class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ROWS = n
        COLS = n
        board = [["."] * COLS for _ in range(ROWS)]
        res = []
        marked_cols = [False] * COLS
        # set([row + col, ...])
        marked_diags = set()
        # set([row - col, ...])
        marked_a_diags2 = set()
        
        def backtrack(row):
            nonlocal res
            if row == ROWS:
                res.append(["".join(row) for row in board])
                return

            for col in range(COLS):
                if (
                    marked_cols[col] or
                    (row + col) in marked_diags or 
                    (row - col) in marked_a_diags2
                ):
                    continue

                board[row][col] = "Q"
                marked_cols[col] = True
                marked_diags.add(row + col)
                marked_a_diags2.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                marked_cols[col] = False
                marked_diags.remove(row + col)
                marked_a_diags2.remove(row - col)
        

        backtrack(0)
        return res


print(Solution().solveNQueens(1) == [["Q"]])
print(Solution().solveNQueens(2) == [])
print(Solution().solveNQueens(3) == [])
print(Solution().solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
print(Solution().solveNQueens(5) == [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."], [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."], ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."], ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."], ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]])
