class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: backtracking
        """
        ROWS = n
        COLS = n
        grid = [['.'] * COLS for _ in range(ROWS)]
        visited_cols = [False] * COLS
        visited_diags = [False] * COLS * 2
        visited_adiags = [False] * COLS * 2

        def backtrack(row):
            if row == ROWS:
                return 1

            res = 0

            for col in range(COLS):
                if (
                    visited_cols[col]
                    or visited_diags[row + col]
                    or visited_adiags[row - col + n]
                ):
                    continue

                grid[row][col] = 'Q'
                visited_cols[col] = True
                visited_diags[row + col] = True
                visited_adiags[row - col + n] = True

                res += backtrack(row + 1)

                grid[row][col] = '.'
                visited_cols[col] = False
                visited_diags[row + col] = False
                visited_adiags[row - col + n] = False

            return res

        return backtrack(0)


print(Solution().totalNQueens(4) == 2)
print(Solution().totalNQueens(1) == 1)
print(Solution().totalNQueens(2) == 0)
print(Solution().totalNQueens(3) == 0)
print(Solution().totalNQueens(5) == 10)
