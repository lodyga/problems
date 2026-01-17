from collections import deque


class Twitter:
    """
    Time complexity:
        O(1): postTweet, follow, unfollow, 
        O(n): getNewsFeed
    Auxiliary space complexity: O(n)
    Tags:
        DS: queue, hash map, hash set
        A: iteration
    """

    def __init__(self):
        self.user_db = set()
        # {follower1: set(followee1, followee2, ...)}
        self.follows = {}
        # {followee1: set(follower1, follower2, ...)}
        self.followed_by = {}
        self.tweets = {}
        self.feeds = {}
        self.timestamp = 0

    def _push_tweet_to_followers(self, userId: int, tweetId: int, author: int) -> None:
        feed = self.feeds[userId]
        feed.append((tweetId, author, self.timestamp))
        if len(feed) > 10:
            feed.popleft()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self._create_user(userId)
        self.tweets[userId].append((tweetId, userId, self.timestamp))
        self._push_tweet_to_followers(userId, tweetId, userId)
        for followeeId in self.followed_by[userId]:
            self._push_tweet_to_followers(followeeId, tweetId, userId)

    def getNewsFeed(self, userId: int) -> list[int]:
        feeds = self.feeds
        if (
            userId not in feeds or
            not feeds[userId]
        ):
            return []

        raw_feed = feeds[userId]
        feed = []
        for index in range(len(raw_feed) - 1, -1, -1):
            feed.append(raw_feed[index][0])
        return feed

    def _update_feed_with_followee(self, followerId: int, followeeId: int) -> None:
        follower_feed = self.feeds[followerId]
        followee_tweets = self.tweets[followeeId]

        updated_feed = deque()
        er_index = len(follower_feed) - 1
        ee_index = len(followee_tweets) - 1
        counter = 0
        while counter < 10 and (er_index > -1 or ee_index > -1):
            if er_index == -1:
                updated_feed.appendleft(followee_tweets[ee_index])
                ee_index -= 1
            elif ee_index == -1:
                updated_feed.appendleft(follower_feed[er_index])
                er_index -= 1
            elif follower_feed[er_index][2] > followee_tweets[ee_index][2]:
                updated_feed.appendleft(follower_feed[er_index])
                er_index -= 1
            else:
                updated_feed.appendleft(followee_tweets[ee_index])
                ee_index -= 1
            counter += 1

        self.feeds[followerId] = updated_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Self follow not allowed.
        if followerId == followeeId:
            return

        self._create_user(followerId)
        self._create_user(followeeId)

        # Already following.
        if followeeId in self.follows[followerId]:
            return

        self.follows[followerId].add(followeeId)
        self.followed_by[followeeId].add(followerId)
        self._update_feed_with_followee(followerId, followeeId)

    def _rebuild_feed(self, followerId: int, followeeId: int) -> None:
        self.feeds[followerId] = self.tweets[followerId]
        while len(self.feeds[followerId]) > 10:
            self.feeds[followerId].popleft()

        for followeeId in self.follows[followerId]:
            self._update_feed_with_followee(followerId, followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Cannot unfollow if not following.
        if followeeId not in self.follows[followerId]:
            return

        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

        if followeeId in self.followed_by:
            self.followed_by[followeeId].discard(followerId)

        self._rebuild_feed(followerId, followeeId)

    def _create_user(self, user_id):
        if user_id in self.user_db:
            return

        self.user_db.add(user_id)
        self.tweets[user_id] = deque()
        self.feeds[user_id] = deque()
        self.follows[user_id] = set()
        self.followed_by[user_id] = set()


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "Twitter":
            cls = Twitter(*argument)
            output.append(None)
        elif operation == "postTweet":
            cls.postTweet(*argument)
            output.append(None)
        elif operation == "getNewsFeed":
            output.append(cls.getNewsFeed(*argument))
        elif operation == "follow":
            cls.follow(*argument)
            output.append(None)
        elif operation == "unfollow":
            cls.unfollow(*argument)
            output.append(None)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["Twitter", "getNewsFeed"],
    ["Twitter", "postTweet", "getNewsFeed", "follow",
        "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
    ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
        "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "getNewsFeed", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
    ["Twitter", "postTweet", "postTweet", "unfollow", "follow", "getNewsFeed"],
    ["Twitter", "postTweet", "follow", "follow", "getNewsFeed"],
    ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
        "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "getNewsFeed", "getNewsFeed", "getNewsFeed", "getNewsFeed", "getNewsFeed"]
]

arguments_list = [
    [[], [1]],
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
    [[], [1, 5], [2, 3], [1, 101], [2, 13], [2, 10], [1, 2], [1, 94], [2, 505], [1, 333], [2, 22], [1, 11], [1, 205], [2, 203], [
        1, 201], [2, 213], [1, 200], [2, 202], [1, 204], [2, 208], [2, 233], [1, 222], [2, 211], [1], [1, 2], [1], [1, 2], [1]],
    [[], [1, 4], [2, 5], [1, 2], [1, 2], [1]],
    [[], [2, 5], [1, 2], [1, 2], [1]],
    [[], [1, 6765], [5, 671], [3, 2868], [4, 8148], [4, 386], [3, 6673], [3, 7946], [3, 1445], [4, 4822], [1, 3781], [4, 9038], [1, 9643], [
        3, 5917], [2, 8847], [1, 3], [1, 4], [4, 2], [4, 1], [3, 2], [3, 5], [3, 1], [2, 3], [2, 1], [2, 5], [5, 1], [5, 2], [1], [2], [3], [4], [5]]
]

expected_output_list = [
    [None, []],
    [None, None, [5], None, None, [6, 5], None, [5]],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [222, 204,
                                                                                                                                                200, 201, 205, 11, 333, 94, 2, 101], None, [211, 222, 233, 208, 204, 202, 200, 213, 201, 203], None, [222, 204, 200, 201, 205, 11, 333, 94, 2, 101]],
    [None, None, None, None, None, [5, 4]],
    [None, None, None, None, [5]],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [5917, 9643, 9038, 3781, 4822, 1445, 7946, 6673,
                                                                                                                                                                        386, 8148], [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765], [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765], [8847, 9643, 9038, 3781, 4822, 386, 8148, 6765], [8847, 9643, 3781, 671, 6765]]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of TimeMap tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            output.append((test_input(operations, arguments), expected_output))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output


print(run_tests(operations_list, arguments_list, expected_output_list))


# Example 1
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1) == [5])
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1) == [6, 5])
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1) == [5])

# Ecample 2
twitter2 = Twitter()
twitter2.postTweet(1, 1)
print(twitter2.getNewsFeed(1) == [1]) 
twitter2.follow(2, 1)
print(twitter2.getNewsFeed(2) == [1]) 
twitter2.unfollow(2, 1)
print(twitter2.getNewsFeed(2) == [])  

# Example 3
twitter3 = Twitter()
print(twitter3.getNewsFeed(1) == [])

# Example 4
twitter4 = Twitter()
twitter4.follow(1, 5)
print(twitter4.getNewsFeed(1) == [])

# Example 5
twitter5 = Twitter()
twitter5.postTweet(1, 5)
twitter5.postTweet(1, 3)
print(twitter5.getNewsFeed(1) == [3, 5])
















# Legacy
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