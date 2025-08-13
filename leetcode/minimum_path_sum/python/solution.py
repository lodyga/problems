class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-dwon
        """
        rows = len(grid)
        cols = len(grid[0])
        memo = [[None] * cols for _ in range(rows)]
        memo[rows - 1][cols - 1] = grid[rows - 1][cols - 1]

        def dfs(row, col):
            if (
                row == rows or
                col == cols
            ):
                return 40000
            elif memo[row][col] is not None:
                return memo[row][col]

            memo[row][col] = grid[row][col] + min(dfs(row + 1, col),
                                                  dfs(row, col + 1))
            return memo[row][col]

        return dfs(0, 0)


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        rows = len(grid)
        cols = len(grid[0])
        cache = [40000] * cols
        cache[-1] = 0

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if col == cols - 1:
                    cache[col] += grid[row][col]
                else:
                    cache[col] = grid[row][col] + min(cache[col], cache[col + 1])

        return cache[0]


print(Solution().minPathSum([[1, 2], [3, 4]]), 7)
print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]), 12)