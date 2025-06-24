import heapq


class Twitter:
    """
    Time complexity: O(n)
        O(1): postTweet, follow, unfollow, 
        O(n): getNewsFeed
    Auxiliary space complexity: O(n)
    Tags: heap
    """
    def __init__(self):
        self.follows = {}  # {followerId: set(followeeId1, ...), ...}
        self.tweets = {}  # {useId: [(timestamp, tweetId), ...], ...}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._create_user(userId)
        user_tweets = self.tweets[userId]
        user_tweets.append((self.timestamp, tweetId))
        if len(user_tweets) > 10:
            user_tweets.pop(0)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:        
        def merge_feed(user):
            if user not in self.tweets:
                return
            elif news_heap and news_heap[0][0] > self.tweets[userId][-1][0]:
                return

            for tweet in self.tweets[user][-10:]:
                if len(news_heap) < 10:
                    heapq.heappush(news_heap, tweet)
                else:
                    heapq.heappushpop(news_heap, tweet)

        news_heap = []
        merge_feed(userId)

        if userId in self.follows:
            for followee in self.follows[userId]:
                merge_feed(followee)

        return list(reversed([heapq.heappop(news_heap)[1] 
                              for _ in range(len(news_heap))]))
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self._create_user(followeeId)
        self._create_user(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

    def _create_user(self, userId):
        if userId not in self.follows:
            self.follows[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = []


import heapq
from collections import deque


class Twitter:
    """
    Time complexity: O(n)
        O(1): postTweet, follow, unfollow, 
        O(n): getNewsFeed
    Auxiliary space complexity: O(n)
    Tags: heap, deque
    """
    def __init__(self):
        self.follows = {}  # {followerId: set(followeeId1, ...), ...}
        self.tweets = {}  # {useId: [tweet counter, deque((timestamp, tweetId), ...), ...}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._create_user(userId)
        user_tweet_count, user_tweets = self.tweets[userId]
        user_tweets.append((self.timestamp, tweetId))

        if user_tweet_count > 10:
            user_tweets.popleft()
        else:
            self.tweets[userId][0] += 1

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:        
        def merge_feed(user):
            if user not in self.tweets:
                return            
            elif news_heap and news_heap[0][0] > self.tweets[userId][1][0][1]:  # [1][0][1] => [deque][(timestamp, tweet)][tweet]
                return

            for tweet in self.tweets[user][1]:
                if len(news_heap) < 10:
                    heapq.heappush(news_heap, tweet)
                else:
                    heapq.heappushpop(news_heap, tweet)

        news_heap = []
        merge_feed(userId)

        if userId in self.follows:
            for followee in self.follows[userId]:
                merge_feed(followee)

        return list(reversed([heapq.heappop(news_heap)[1] 
                              for _ in range(len(news_heap))]))
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self._create_user(followeeId)
        self._create_user(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

    def _create_user(self, userId):
        if userId not in self.follows:
            self.follows[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = [0, deque()]
        


def test_input(operations: list[str], arguments: list[list[int | None]]) -> list[list[int] | None]:
    """
    Test imput provided in two separate lists: operations and arguments
    """
    twitter = None
    result = []
    
    for operation, argument in zip(operations, arguments):
        if operation == "Twitter":
            twitter = Twitter()
            result.append(None)
        elif operation == "postTweet":
            result.append(twitter.postTweet(*argument))
        elif operation == "getNewsFeed":
            result.append(twitter.getNewsFeed(*argument))
        elif operation == "follow":
            result.append(twitter.follow(*argument))
        elif operation == "unfollow":
            result.append(twitter.unfollow(*argument))

    return result

# Example Input
operations = ["Twitter", "getNewsFeed"]
arguments = [[], [1]]
expected_output = [None, []]

operations = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
arguments = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
expected_output = [None, None, [5], None, None, [6, 5], None, [5]]

operations = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
arguments = [[],[1,5],[2,3],[1,101],[2,13],[2,10],[1,2],[1,94],[2,505],[1,333],[2,22],[1,11],[1,205],[2,203],[1,201],[2,213],[1,200],[2,202],[1,204],[2,208],[2,233],[1,222],[2,211],[1],[1,2],[1],[1,2],[1]]
expected_output = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[222,204,200,201,205,11,333,94,2,101],None,[211,222,233,208,204,202,200,213,201,203],None,[222,204,200,201,205,11,333,94,2,101]]


# Run tests
actual_output = test_input(operations, arguments)
print(actual_output == expected_output)
# print(actual_output)



twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)  # User 1 follows user 2.
twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

twitter2 = Twitter()
twitter2.postTweet(1, 1)
print(twitter2.getNewsFeed(1))  # [1]
twitter2.follow(2, 1)
print(twitter2.getNewsFeed(2))  # [1]
twitter2.unfollow(2, 1)
print(twitter2.getNewsFeed(2))  # []

twitter3 = Twitter()
print(twitter3.getNewsFeed(1))  # []

twitter4 = Twitter()
twitter4.follow(1, 5)
print(twitter4.getNewsFeed(1))  # []

twitter5 = Twitter()
twitter5.postTweet(1, 5)
twitter5.postTweet(1, 3)
print(twitter5.getNewsFeed(1))  # [3, 5]