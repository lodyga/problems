import { Queue } from '@datastructures-js/queue';
import { MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Time complexity: O(n)
 *    O(1): postTweet, follow, unfollow, 
 *    O(n): getNewsFeed
 * Auxiliary space complexity: O(n)
 * Tags: heap
 */
class Twitter {
   constructor() {
      this.follows = new Map();  // {followerId: Set(followeeId1, ...), ...}
      this.tweets = new Map();  // Map(useId: [(timestamp, tweetId), ...], ...)
      this.timestamp = 0;
   }

   postTweet(userId, tweetId) {
      this._createUser(userId);
      this.tweets.get(userId).push([this.timestamp, tweetId]);
      this.timestamp++;

   };

   getNewsFeed(userId) {
      const mergeFeed = (user) => {
         const userTweets = this.tweets.get(user);
         if (!userTweets || userTweets.length === 0)
            return;
         else if (
            newsHeap.length &&
            newsHeap.front()[0] > userTweets[userTweets.length - 1][0]
         ) {
            return
         }
         for (let index = userTweets.length - 1; index >= Math.max(0, userTweets.length - 10); index--) {
            const tweet = userTweets[index];
            newsHeap.push(tweet);
            if (newsHeap.size() > 10) {
               newsHeap.pop();
            }
         }
      }

      const newsHeap = new MinPriorityQueue(x => x[0]);
      mergeFeed(userId)

      if (this.follows.has(userId)) {
         for (const followee of this.follows.get(userId)) {
            mergeFeed(followee);
         }
      }

      return newsHeap.toArray().reverse().map(([_, tweetId]) => tweetId)
   };

   follow(followerId, followeeId) {
      if (followerId === followeeId) {
         return
      }

      this._createUser(followerId);
      this._createUser(followeeId);
      this.follows.get(followerId).add(followeeId);
   };

   unfollow(followerId, followeeId) {
      if (this.follows.has(followerId)) {
         this.follows.get(followerId).delete(followeeId);
      }
   };

   _createUser(userId) {
      if (!this.tweets.has(userId)) {
         this.tweets.set(userId, []);
      }
      if (!this.follows.has(userId)) {
         this.follows.set(userId, new Set());
      }
   }
}


const twitter = new Twitter();
twitter.postTweet(1, 5);  // User 1 posts a new tweet (id = 5).
console.log(twitter.getNewsFeed(1));  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);  // User 1 follows user 2.
twitter.postTweet(2, 6);  // User 2 posts a new tweet (id = 6).
console.log(twitter.getNewsFeed(1));  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
console.log(twitter.getNewsFeed(1));  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

const twitter2 = new Twitter()
twitter2.postTweet(1, 1)
console.log(twitter2.getNewsFeed(1))  // [1]
twitter2.follow(2, 1)
console.log(twitter2.getNewsFeed(2))  // [1]
twitter2.unfollow(2, 1)
console.log(twitter2.getNewsFeed(2))  // []

const twitter3 = new Twitter()
console.log(twitter3.getNewsFeed(1))  // []

const twitter4 = new Twitter()
twitter4.follow(1, 5)
console.log(twitter4.getNewsFeed(1))  // []

const twitter5 = new Twitter()
twitter5.postTweet(1, 5)
twitter5.postTweet(1, 3)
console.log(twitter5.getNewsFeed(1))  // [3, 5]