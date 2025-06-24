r"""
draft

[1, 4, 2]
 |    \
[1, 2, 4]
[1, 2], [1, 4]

[2,  5, 1, 2, 5]
     |    \   |
[10, 5, 2, 1, 5, 2]
[2, 5, 2], [5, 1, 5], [5, 1, 2]
"""


class Solution:
    def maxUncrossedLines(self, numbers1: list[int], numbers2: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index1, index2):
            if (
                index1 == len(numbers1) or
                index2 == len(numbers2)
            ):
                return 0

            if numbers1[index1] == numbers2[index2]:
                memo = dfs(index1 + 1, index2 + 1) + 1
            else:
                memo = max(
                    dfs(index1 + 1, index2),
                    dfs(index1, index2 + 1)
                )

            return memo

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, numbers1: list[int], numbers2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        dp, top-down with memoization as hash map
        """
        memo = {}  # {(index1, index2): number of connections}

        def dfs(index1, index2):
            if (
                index1 == len(numbers1) or
                index2 == len(numbers2)
            ):
                return 0
            elif (index1, index2) in memo:
                return memo[(index1, index2)]

            if numbers1[index1] == numbers2[index2]:
                memo[(index1, index2)] = dfs(index1 + 1, index2 + 1) + 1
            else:
                memo[(index1, index2)] = max(
                    dfs(index1 + 1, index2),
                    dfs(index1, index2 + 1)
                )

            return memo[(index1, index2)]

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, numbers1: list[int], numbers2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        dp, top-down with memoization as array
        """
        # [(index_1, index_2): number of connections]
        memo = [[None] * len(numbers2) 
                for _ in range(len(numbers1))]

        def dfs(index1, index2):
            if (
                index1 == len(numbers1) or
                index2 == len(numbers2)
            ):
                return 0
            elif memo[index1][index2] is not None:
                return memo[index1][index2]

            if numbers1[index1] == numbers2[index2]:
                memo[index1][index2] = dfs(index1 + 1, index2 + 1) + 1
            else:
                memo[index1][index2] = max(
                    dfs(index1 + 1, index2),
                    dfs(index1, index2 + 1)
                )

            return memo[index1][index2]

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, numbers1: list[int], numbers2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        dp, bottom-up
        """
        # [(index_1, index_2): number of connections]
        cache = [[0] * (len(numbers2) + 1) 
                 for _ in range(len(numbers1) + 1)]
        
        for index1 in reversed(range(len(numbers1))):
            for index2 in reversed(range(len(numbers2))):
                if numbers1[index1] == numbers2[index2]:
                    cache[index1][index2] = cache[index1 + 1][index2 + 1] + 1
                else:
                    cache[index1][index2] = max(
                        cache[index1 + 1][index2],
                        cache[index1][index2 + 1]
                    )

        return cache[0][0]


print(Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2)
print(Solution().maxUncrossedLines([1, 5, 6], [5, 6]) == 2)
print(Solution().maxUncrossedLines([5, 6], [1, 5, 6]) == 2)
print(Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3)
print(Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2)
print(Solution().maxUncrossedLines([4, 1, 2, 5, 1, 5, 3, 4, 1, 5], [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]) == 7)
print(Solution().maxUncrossedLines([5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1], [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]) == 11)