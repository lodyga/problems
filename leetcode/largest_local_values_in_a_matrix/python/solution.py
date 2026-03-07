class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        (ROWS, COLS) = (len(grid) - 2, len(grid[0]) - 2)
        res = [[0] * COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                m = 0

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        m = max(m, grid[r][c])

                res[row][col] = m

        return res


print(Solution().largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]) == [[9, 9], [8, 6]])
print(Solution().largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
