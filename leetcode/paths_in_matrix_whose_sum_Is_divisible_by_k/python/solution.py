class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-down
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        MOD = 10**9 + 7
        # memo[row][col][r] = number of ways to reach bottom-right with remainder r at this cell
        memo = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col, reminder):
            if (
                row == ROWS or
                col == COLS
            ):
                return 0

            reminder = (reminder + grid[row][col]) % k

            if (row, col) == (ROWS - 1, COLS - 1):
                return 1 if reminder == 0 else 0

            if memo[row][col][reminder] != -1:
                return memo[row][col][reminder]

            down = dfs(row + 1, col, reminder)
            right = dfs(row, col + 1, reminder)

            memo[row][col][reminder] = (down + right) % MOD
            return memo[row][col][reminder]

        return dfs(0, 0, 0)


print(Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2)
print(Solution().numberOfPaths([[0, 0]], 5) == 1)
print(Solution().numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10)
print(Solution().numberOfPaths([[0]], 1) == 1)
