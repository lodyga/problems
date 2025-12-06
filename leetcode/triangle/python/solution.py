class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up, in-place
        """
        for row in reversed(range(len(triangle) - 1)):
            for col in range(row + 1):
                triangle[row][col] += min(triangle[row + 1][col],
                                          triangle[row + 1][col + 1])

        return triangle[0][0]


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up, in-place
        """
        for row in range(1, len(triangle)):
            triangle[row][0] += triangle[row - 1][0]
            triangle[row][-1] += triangle[row - 1][-1]

            for col in range(1, row):
                triangle[row][col] += min(triangle[row - 1][col - 1],
                                          triangle[row - 1][col])

        return min(triangle[-1])


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(1)
        Tags: brute-force, tle
        """
        def dfs(level: int, index: int) -> int:
            if level == len(triangle):
                return 0
            else:
                return (triangle[level][index] +
                        min(dfs(level + 1, index),
                            dfs(level + 1, index + 1)))

        return dfs(0, 0)


print(Solution().minimumTotal([[2]]) == 2)
print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11)
print(Solution().minimumTotal([[-10]]) == -10)