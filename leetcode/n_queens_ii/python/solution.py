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
        counter = 0
        visited_cols = [False] * COLS
        # [row + col, ...]
        visited_diags = [False] * (ROWS + COLS - 1)
        # [row - col + n, ...]
        visited_adiags = [False] * (ROWS + COLS)

        def backtrack(row):
            nonlocal counter
            if row == ROWS:
                counter += 1
                return

            for col in range(COLS):
                if (
                    visited_cols[col] or
                    visited_diags[row + col] or
                    visited_adiags[row - col + n]
                ):
                    continue

                visited_cols[col] = True
                visited_diags[row + col] = True
                visited_adiags[row - col + n] = True

                backtrack(row + 1)

                visited_cols[col] = False
                visited_diags[row + col] = False
                visited_adiags[row - col + n] = False

        backtrack(0)
        return counter


print(Solution().totalNQueens(1) == 1)
print(Solution().totalNQueens(2) == 0)
print(Solution().totalNQueens(3) == 0)
print(Solution().totalNQueens(4) == 2)
print(Solution().totalNQueens(5) == 10)
