class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        def validate_rows():
            for row in range(9):
                cells = [False] * 9

                for col in range(9):
                    cell = board[row][col]
                    if cell == ".":
                        continue

                    val = int(cell)
                    if cells[val - 1]:
                        return False
                    else:
                        cells[val - 1] = True

            return True

        def validate_cols():
            for col in range(9):
                cells = [False] * 9

                for row in range(9):
                    cell = board[row][col]
                    if cell == ".":
                        continue

                    val = int(cell)
                    if cells[val - 1]:
                        return False
                    else:
                        cells[val - 1] = True

            return True

        def validate_subboxes():
            def validate_subbox(row, col):
                cells = [False] * 9

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        cell = board[r][c]
                        if cell == ".":
                            continue

                        val = int(cell)
                        if cells[val - 1]:
                            return False
                        else:
                            cells[val - 1] = True
                
                return True

            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    if validate_subbox(row, col) is False:
                        return False

            return True

        return (
            validate_rows() and
            validate_cols() and
            validate_subboxes()
        )


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set, built-in data structure
            A: iteration
        """
        from collections import defaultdict

        row_uniq = defaultdict(set)
        col_uniq = defaultdict(set)
        box_uniq = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]

                if cell == ".":
                    continue
                elif (
                    cell in row_uniq[row] or
                    cell in col_uniq[col] or
                    cell in box_uniq[(row//3, col//3)]
                ):
                    return False
                else:
                    row_uniq[row].add(cell)
                    col_uniq[col].add(cell)
                    box_uniq[(row//3, col//3)].add(cell)

        return True


print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == True)
print(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == False)
print(Solution().isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"],  ["8", ".", ".", ".", ".", ".", ".", "2", "."],  [".", ".", "2", ".", "7", ".", ".", ".", "."],  [".", "1", "5", ".", ".", ".", ".", ".", "."],  [".", ".", ".", ".", ".", "2", ".", ".", "."],  [".", "2", ".", "9", ".", ".", ".", ".", "."],  [".", ".", "4", ".", ".", ".", ".", ".", "."]]) == False)
