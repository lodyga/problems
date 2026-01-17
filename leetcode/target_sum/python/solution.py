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
        memo = {}

        def dfs(index: int, total: int) -> int:
            memo_ind = (index, total)

            if index == len(nums):
                return total == target
            elif memo_ind in memo:
                return memo[memo_ind]

            num = nums[index]
            add_num = dfs(index + 1, total + num)
            subtract_num = dfs(index + 1, total - num)
            memo[memo_ind] = add_num + subtract_num
            return memo[memo_ind]

        return dfs(0, 0)


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        N = len(nums)
        # [[dict(index, total): counter (ways to get total using `index` nums), ][index], ]
        cache = [defaultdict(int) for _ in range(N + 1)]
        cache[0][0] = 1

        for index in range(N):
            num = nums[index]
            for total, counter in cache[index].items():
                cache[index + 1][total + num] += counter
                cache[index + 1][total - num] += counter

        return cache[N][target]


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*m)
            n: num count
            m: num sum
        Auxiliary space complexity: O(m)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)
        # [[dict(total): counter (ways to get total using `index` nums), ], ]
        cache = defaultdict(int)
        cache[0] = 1

        for num in nums:
            next_cache = defaultdict(int)
            for total, counter in cache.items():
                next_cache[total + num] += counter
                next_cache[total - num] += counter
            cache = next_cache

        return cache[target]


print(Solution().findTargetSumWays([1], 1) == 1)
print(Solution().findTargetSumWays([2, 2, 2], 2) == 3)
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
print(Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) == 5115)
