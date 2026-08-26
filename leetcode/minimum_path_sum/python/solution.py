class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-dwon
        """
        def dfs(row, col) -> int:
            if (row >= ROWS or col >= COLS):
                return INF
            elif memo[row][col] != -1:
                return memo[row][col]

            res = grid[row][col] \
                + min(
                    dfs(row + 1, col),
                    dfs(row, col + 1)
            )
            memo[row][col] = res

            return res

        INF = 10**7
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        memo[-1][-1] = grid[-1][-1]
        return dfs(0, 0)


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        INF = 10**7
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = [[INF] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[-1][-2] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                cache[row][col] = grid[row][col] \
                    + min(cache[row + 1][col],
                          cache[row][col + 1]
                          )

        return cache[0][0]


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        INF = 10**7
        ROWS = len(grid)
        COLS = len(grid[0])
        next_cache = [INF] * (COLS + 1)
        next_cache[-2] = 0

        for row in range(ROWS - 1, -1, -1):
            cache = [INF] * (COLS + 1)

            for col in range(COLS - 1, -1, -1):
                cache[col] = grid[row][col] \
                    + min(next_cache[col], cache[col + 1])

            next_cache = cache

        return next_cache[0]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) == 12)
print(Solution().minPathSum([[1, 2], [3, 4]]) == 7)
