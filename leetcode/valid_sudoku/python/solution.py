from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
            A: iteration
        """
        ROWS = len(board)
        COLS = len(board[0])

        def are_rows_valid() -> bool:
            for row in range(ROWS):
                row_values = set()

                for col in range(COLS):
                    cell = board[row][col]
                    if cell == ".":
                        continue
                    elif cell in row_values:
                        return False
                    else:
                        row_values.add(cell)
            return True

        def are_cols_valid() -> bool:
            for col in range(COLS):
                col_values = set()

                for row in range(ROWS):
                    cell = board[row][col]
                    if cell == ".":
                        continue
                    elif cell in col_values:
                        return False
                    else:
                        col_values.add(cell)
            return True

        def are_boxes_valid() -> bool:
            def is_box_valid(row, col):
                box_values = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        cell = board[i][j]
                        if cell == ".":
                            continue
                        elif cell in box_values:
                            return False
                        else:
                            box_values.add(cell)
                return True

            for row in range(0, ROWS, 3):
                for col in range(0, COLS, 3):
                    if is_box_valid(row, col) is False:
                        return False
            return True

        return (
            are_rows_valid() and
            are_cols_valid() and
            are_boxes_valid()
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
        ROWS = len(board)
        COLS = len(board[0])

        row_uniq = defaultdict(set)
        col_uniq = defaultdict(set)
        box_uniq = defaultdict(set)

        for row in range(ROWS):
            for col in range(COLS):
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
