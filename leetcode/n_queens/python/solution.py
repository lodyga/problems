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
        Tags: backtracking
        """
        rows = n
        cols = n
        board_list = []
        visited_cols = set()
        visited_diags = set()  # set(row + col, ...)
        visited_adiags = set()  # set(row - col, ...)
        board = [["."] * cols for _ in range(rows)]

        def dfs(row):
            if row == rows:
                board_list.append(["".join(row) for row in board])
                return

            for col in range(cols):
                if (
                    col in visited_cols or
                    row + col in visited_diags or
                    row - col in visited_adiags
                ):
                    continue

                visited_cols.add(col)
                visited_diags.add(row + col)
                visited_adiags.add(row - col)
                board[row][col] = "Q"
                dfs(row + 1)
                visited_cols.remove(col)
                visited_diags.remove(row + col)
                visited_adiags.remove(row - col)
                board[row][col] = "."

        dfs(0)
        return board_list


print(Solution().solveNQueens(1) == [["Q"]])
print(Solution().solveNQueens(2) == [])
print(Solution().solveNQueens(3) == [])
print(Solution().solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
print(Solution().solveNQueens(5) == [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."], [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."], ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."], ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."], ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]])