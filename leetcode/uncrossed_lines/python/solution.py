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
        N1 = len(nums1)
        N2 = len(nums2)
        # {(idx1, idx2): connection counter}
        memo = {}

        def dfs(idx1: int, idx2: int) -> int:
            idx = (idx1, idx2)
            idx = idx1 << 32 | idx2
            if idx1 == N1 or idx2 == N2:
                return 0
            elif idx in memo:
                return memo[idx]

            num1 = nums1[idx1]
            num2 = nums2[idx2]

            if num1 == num2:
                res = 1 + dfs(idx1 + 1, idx2 + 1)
            else:
                res = max(
                    dfs(idx1 + 1, idx2),
                    dfs(idx1, idx2 + 1)
                )

            memo[idx] = res
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
        N1 = len(nums1)
        N2 = len(nums2)
        # [(idx1, idx2): connection count, ]
        memo = [[-1] * N2 for _ in range(N1)]

        def dfs(idx1: int, idx2: int) -> int:
            if idx1 == N1 or idx2 == N2:
                return 0
            elif memo[idx1][idx2] != -1:
                return memo[idx1][idx2]

            num1 = nums1[idx1]
            num2 = nums2[idx2]

            if num1 == num2:
                res = 1 + dfs(idx1 + 1, idx2 + 1)
            else:
                res = max(
                    dfs(idx1 + 1, idx2),
                    dfs(idx1, idx2 + 1)
                )

            memo[idx1][idx2] = res
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
        N1 = len(nums1)
        N2 = len(nums2)
        # [(idx1, idx2): connection count]
        cache = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        for idx1 in range(N1 - 1, -1, -1):
            for idx2 in range(N2 - 1, -1, -1):

                num1 = nums1[idx1]
                num2 = nums2[idx2]

                if num1 == num2:
                    cache[idx1][idx2] = 1 + cache[idx1 + 1][idx2 + 1]
                else:
                    cache[idx1][idx2] = max(
                        cache[idx1 + 1][idx2],
                        cache[idx1][idx2 + 1]
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
        N1 = len(nums1)
        N2 = len(nums2)
        # {idx2: connection count}
        next_cache = [0] * (N2 + 1)

        for idx1 in range(N1 - 1, -1, -1):
            cache = [0] * (N2 + 1)

            for idx2 in range(N2 - 1, -1, -1):
                if nums1[idx1] == nums2[idx2]:
                    cache[idx2] = 1 + next_cache[idx2 + 1]
                else:
                    cache[idx2] = max(
                        next_cache[idx2],
                        cache[idx2 + 1]
                    )

            next_cache = cache

        return next_cache[0]


print(Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2)
print(Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3)
print(Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2)
print(Solution().maxUncrossedLines([1, 5, 6], [5, 6]) == 2)
print(Solution().maxUncrossedLines([5, 6], [1, 5, 6]) == 2)
print(Solution().maxUncrossedLines([4, 1, 2, 5, 1, 5, 3, 4, 1, 5], [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]) == 7)
print(Solution().maxUncrossedLines([1, 2, 4, 1, 4, 4, 3, 5, 5, 1, 4, 4, 4, 1, 4, 3, 4, 2, 4, 2], [2, 4, 1, 1, 3, 5, 2, 1, 5, 1, 2, 3, 3, 2, 1, 4, 1, 2, 5, 5]) == 11)
print(Solution().maxUncrossedLines([5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1], [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]) == 11)
