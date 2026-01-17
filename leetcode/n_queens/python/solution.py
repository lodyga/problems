r"""
draft
elements with the same num are on the same diagonal
    0   1   2
0   0   1   2
1   -1  0   1
2   -2  -1  0

elements with the same num are on the same anti-diagonal
    0   1   2
0   0   1   2
1   1   2   3
2   2   3   4
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), hash set
            A: DFS with backtracking
        """
        ROWS = n
        COLS = n
        visited_cols = [False] * COLS
        visited_diags = set()  # set(row + col, ...)
        visited_adiags = set()  # set(row - col, ...)
        board = [["."] * COLS for _ in range(ROWS)]
        board_list = []

        def backtrack(row):
            if row == ROWS:
                board_list.append(["".join(row) for row in board])
                return

            for col in range(COLS):
                if (
                    visited_cols[col] or
                    row + col in visited_diags or
                    row - col in visited_adiags
                ):
                    continue
                
                board[row][col] = "Q"
                visited_cols[col] = True
                visited_diags.add(row + col)
                visited_adiags.add(row - col)
                backtrack(row + 1)
                board[row][col] = "."
                visited_cols[col] = False
                visited_diags.discard(row + col)
                visited_adiags.discard(row - col)

        backtrack(0)
        return board_list


print(Solution().solveNQueens(1) == [["Q"]])
print(Solution().solveNQueens(2) == [])
print(Solution().solveNQueens(3) == [])
print(Solution().solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
print(Solution().solveNQueens(5) == [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."], [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."], ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."], ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."], ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]])
