class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n4)
        Auxiliary space complexity: O(n4)
        Tags:
            DS: array (matrix)
            A: top-dwon
        """
        INF = float("inf")
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = [[[[-1] * COLS for _ in range(ROWS)]
                  for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row1, col1, row2, col2):
            if (
                row1 in (-1, ROWS) or
                col1 in (-1, COLS) or
                grid[row1][col1] == -1 or
                row2 in (-1, ROWS) or
                col2 in (-1, COLS) or
                grid[row2][col2] == -1 or
                (row1 + col1) != (row2 + col2)
            ):
                return -INF
            elif (row1, col1) == (row2, col2) == (ROWS - 1, COLS - 1):
                return grid[row1][col1]
            elif cache[row1][col1][row2][col2] != -1:
                return cache[row1][col1][row2][col2]

            res = dfs(row1 + 1, col1, row2 + 1, col2)
            res = max(res, dfs(row1, col1 + 1, row2, col2 + 1))
            res = max(res, dfs(row1 + 1, col1, row2, col2 + 1))
            res = max(res, dfs(row1, col1 + 1, row2 + 1, col2))
            res += grid[row1][col1]
            res += grid[row2][col2] if (row2, col2) != (row1, col1) else 0
            cache[row1][col1][row2][col2] = res
            return res
        
        return max(dfs(0, 0, 0, 0), 0)


print(Solution().cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5)
print(Solution().cherryPickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0)
print(Solution().cherryPickup([[1, 1, 1, 1, -1, -1, -1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, -1, 1, 1], [0, 0, 0, 0, 1, -1, 0, 0, 1, -1], [1, 0, 1, 1, 1, 0, 0, -1, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, -1], [1, -1, 0, 1, 0, 0, 0, 1, -1, 1], [1, 0, -1, 0, -1, 0, 0, 1, 0, 0], [0, 0, -1, 0, 1, 0, 1, 0, 0, 1]]) == 22)
print(Solution().cherryPickup([[1, -1, 1, 1, 1, 1, 1, 1, -1, 1], [1, 1, 1, 1, -1, -1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [1, 1, -1, 1, -1, 1, 1, 1, 1, 1], [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, 1, 1, 1, -1, 1, 1, -1, 1], [1, 1, 1, 1, 1, 1, 1, -1, 1, 1], [1, 1, 1, 1, -1, 1, -1, -1, 1, 1], [1, -1, 1, -1, -1, 1, 1, -1, 1, -1], [-1, 1, -1, 1, -1, 1, 1, 1, 1, 1]]) == 23)
