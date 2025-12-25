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
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: hash map
            A: top-down
        """
        # {(index1, index2): connection count}
        memo = {}

        def dfs(index1: int, index2: int) -> int:
            index = (index1, index2)
            if (
                index1 == len(nums1) or
                index2 == len(nums2)
            ):
                return 0
            elif index in memo:
                return memo[index]

            if nums1[index1] == nums2[index2]:
                res = 1 + dfs(index1 + 1, index2 + 1)
            else:
                res = dfs(index1 + 1, index2)
                res = max(res, dfs(index1, index2 + 1))

            memo[index] = res
            return res

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
        """
        # {(index1, index2): connection count}
        memo = [[-1] * len(nums2) for _ in range(len(nums1))]

        def dfs(index1: int, index2: int) -> int:
            if (
                index1 == len(nums1) or
                index2 == len(nums2)
            ):
                return 0
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            if nums1[index1] == nums2[index2]:
                res = 1 + dfs(index1 + 1, index2 + 1)
            else:
                res = dfs(index1 + 1, index2)
                res = max(res, dfs(index1, index2 + 1))

            memo[index1][index2] = res
            return res

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        # {(index1, index2): connection count}
        cache = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for index1 in range(len(nums1) - 1, -1, -1):
            for index2 in range(len(nums2) - 1, -1, -1):

                if nums1[index1] == nums2[index2]:
                    cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                else:
                    cache[index1][index2] = max(
                        cache[index1 + 1][index2],
                        cache[index1][index2 + 1]
                    )

        return cache[0][0]


class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        # {index2: connection count}
        next_cache = [0] * (len(nums2) + 1)

        for index1 in range(len(nums1) - 1, -1, -1):
            cache = [0] * (len(nums2) + 1)

            for index2 in range(len(nums2) - 1, -1, -1):
                if nums1[index1] == nums2[index2]:
                    cache[index2] = 1 + next_cache[index2 + 1]
                else:
                    cache[index2] = max(
                        next_cache[index2],
                        cache[index2 + 1]
                    )
            next_cache = cache

        return next_cache[0]


print(Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2)
print(Solution().maxUncrossedLines([1, 5, 6], [5, 6]) == 2)
print(Solution().maxUncrossedLines([5, 6], [1, 5, 6]) == 2)
print(Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3)
print(Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2)
print(Solution().maxUncrossedLines([4, 1, 2, 5, 1, 5, 3, 4, 1, 5], [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]) == 7)
print(Solution().maxUncrossedLines([1, 2, 4, 1, 4, 4, 3, 5, 5, 1, 4, 4, 4, 1, 4, 3, 4, 2, 4, 2], [2, 4, 1, 1, 3, 5, 2, 1, 5, 1, 2, 3, 3, 2, 1, 4, 1, 2, 5, 5]) == 11)
print(Solution().maxUncrossedLines([5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1], [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]) == 11)
