class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """
        Time complexity: O(n3)
            O(n*m*k)
        Auxiliary space complexity: O(n3)
            O(n*m*k)
        Tags:
            DS: array (matrix)
            A: top-down
        """
        MOD = 10**9 + 7
        ROWS, COLS = len(grid), len(grid[0])
        # memo[row][col][r]: Number of ways to reach bottom-right with remainder at this cell.
        memo = [[[-1] * k
                for _ in range(COLS)]
                for _ in range(ROWS)]

        def dfs(row: int, col: int, rem: int) -> int:
            if row == ROWS or col == COLS:
                return 0

            cell = grid[row][col]
            rem = (rem + cell) % k

            if (row, col) == (ROWS - 1, COLS - 1):
                return 1 if rem == 0 else 0
            elif memo[row][col][rem] != -1:
                return memo[row][col][rem]

            right = dfs(row, col + 1, rem)
            down = dfs(row + 1, col, rem)
            res = (right + down) % MOD
            memo[row][col][rem] = res
            return res

        return dfs(0, 0, 0)


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """
        Time complexity: O(n3)
            O(n*m*k)
        Auxiliary space complexity: O(n3)
            O(n*m*k)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        MOD = 10**9 + 7
        ROWS, COLS = len(grid), len(grid[0])
        # cache[row][col][r]: Number of ways to reach bottom-right with remainder at this cell.
        cache = [[[0] * k
                 for _ in range(COLS + 1)]
                 for _ in range(ROWS + 1)]
        cache[ROWS][COLS - 1][0] = 1

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                for r in range(k):
                    cell = grid[row][col]

                    cache[row][col][(r + cell) % k] = (
                        cache[row + 1][col][r] +
                        cache[row][col + 1][r]
                    ) % MOD

        return cache[0][0][0]


print(Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2)
print(Solution().numberOfPaths([[0, 0]], 5) == 1)
print(Solution().numberOfPaths([[0]], 1) == 1)
print(Solution().numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10)
