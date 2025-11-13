class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index):
            if index == len(nums):
                return 0

            max_num = nums[index]
            partition_sum = 0

            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                partition_sum = max(
                    partition_sum,
                    max_num * (i2 - index + 1) + dfs(i2 + 1)
                )
            return partition_sum

        return dfs(0)


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memization as hash map
        """
        # memo[i] stores max sum starting from index i
        memo = {len(nums): 0}

        def dfs(index):
            if index in memo:
                return memo[index]

            max_num = nums[index]

            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                memo[index] = max(
                    memo.get(index, 0),
                    max_num * (i2 - index + 1) + dfs(i2 + 1)
                )
            return memo[index]

        return dfs(0)


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memization as array
        """
        # memo[i] stores max sum starting from index i
        memo = [-1] * (len(nums) + 1)
        memo[-1] = 0

        def dfs(index):
            if memo[index] != -1:
                return memo[index]

            max_num = nums[index]

            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                memo[index] = max(
                    memo[index],
                    max_num * (i2 - index + 1) + dfs(i2 + 1)
                )
            return memo[index]

        return dfs(0)


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # cache[i] stores max sum starting from index i
        cache = [0] * (len(nums) + 1)

        for index in reversed(range(len(nums))):
            max_num = nums[index]
            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                cache[index] = max(
                    cache[index],
                    max_num * (i2 - index + 1) + cache[i2 + 1]
                )
        return cache[0]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(k)
        Tags: dp, bottom-up
        """
        # cache[i] stores max sum starting from index i
        cache = [0] * k

        for index in reversed(range(len(nums))):
            max_num = nums[index]
            ith_cache = 0
            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                ith_cache = max(
                    ith_cache,
                    max_num * (i2 - index + 1) + cache[i2 - index]
                )
            for i2 in reversed(range(1, k)):
                cache[i2] = cache[i2 - 1]
            cache[0] = ith_cache

        return cache[0]


from collections import deque
class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(k)
        Tags: dp, bottom-up
        """
        # cache[i % k] stores max sum starting from index i
        cache = deque([0] * k)

        for index in reversed(range(len(nums))):
            max_num = nums[index]
            ith_cache = 0
            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                ith_cache = max(
                    ith_cache,
                    max_num * (i2 - index + 1) + cache[i2 - index]
                )
            cache.pop()
            cache.appendleft(ith_cache)

        return cache[0]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(k)
        Tags: dp, bottom-up
        """
        # cache[i] stores max sum starting from index i
        N = len(nums)
        cache = [0] * k
        start = 0

        for index in reversed(range(N)):
            max_num = nums[index]
            ith_cache = 0
            for i2 in range(index, min(index + k, N)):
                max_num = max(max_num, nums[i2])
                ith_cache = max(
                    ith_cache,
                    max_num * (i2 - index + 1) +
                    cache[(i2 - index + start) % k]
                )
            start = (start - 1) % k
            cache[start] = ith_cache

        return cache[start]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(k)
        Tags: dp, bottom-up
        """
        # cache[i % k] stores max sum starting from index i
        cache = [0] * k

        for index in reversed(range(len(nums))):
            max_num = nums[index]
            ith_cache = 0
            for i2 in range(index, min(index + k, len(nums))):
                max_num = max(max_num, nums[i2])
                ith_cache = max(
                    ith_cache,
                    max_num * (i2 - index + 1) + cache[(i2 + 1) % k]
                )
            cache[index % k] = ith_cache

        return cache[0]


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3) == 84)
print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4) == 83)
print(Solution().maxSumAfterPartitioning([1], 1) == 1)
