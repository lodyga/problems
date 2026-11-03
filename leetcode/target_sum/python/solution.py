from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash map
            A: top-down
        """
        def dfs(idx: int, total: int) -> int:
            key = (idx, total)

            if idx == N:
                return total == target
            elif key in memo:
                return memo[key]

            val = nums[idx]
            memo[key] = dfs(idx + 1, total + val)
            memo[key] += dfs(idx + 1, total - val)
            return memo[key]

        N = len(nums)
        memo = {}
        return dfs(0, 0)


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: array, hash map
            A: bottom-up
        """
        N = len(nums)
        # [[dict(idx, total): counter (ways to get total using `idx` nums), ][idx], ]
        cache = [defaultdict(int) for _ in range(N + 1)]
        cache[N][0] = 1

        for idx in range(N - 1, -1, -1):
            val = nums[idx]

            for total, counter in cache[idx + 1].items():
                cache[idx][total + val] += counter
                cache[idx][total - val] += counter

        return cache[0][target]


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: array, hash map
            A: bottom-up
        """
        N = len(nums)
        # [[dict(idx, total): counter (ways to get total using `idx` nums), ][idx], ]
        cache = [defaultdict(int) for _ in range(N + 1)]
        cache[0][0] = 1

        for idx in range(N):
            val = nums[idx]

            for total, counter in cache[idx].items():
                cache[idx + 1][total + val] += counter
                cache[idx + 1][total - val] += counter

        return cache[N][target]


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(m)
        Tags:
            DS: hash map
            A: bottom-up
        """
        N = len(nums)
        # [[dict(total): counter (ways to get total using `idx` nums), ], ]
        cache = defaultdict(int)
        cache[0] = 1

        for num in nums:
            next_cache = defaultdict(int)

            for total, counter in cache.items():
                next_cache[total + num] += counter
                next_cache[total - num] += counter

            cache = next_cache

        return cache[target]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
print(Solution().findTargetSumWays([1], 1) == 1)
print(Solution().findTargetSumWays([2, 2, 2], 2) == 3)
print(Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) == 5115)
