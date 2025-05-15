class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: hash set
        """
        rows = len(board)
        cols = len(board[0])

        def is_row_valid(row):
            unique_numbers = set()
            for char in board[row]:
                if char != ".":
                    if char in unique_numbers:
                        return False
                    else:
                        unique_numbers.add(char)
            return True

        def is_col_valid(col):
            unique_numbers = set()
            for row in range(rows):
                char = board[row][col]
                if char != ".":
                    if char in unique_numbers:
                        return False
                    else:
                        unique_numbers.add(char)
            return True

        def is_subbox_valid(row, col):
            unique_numbers = set()
            for r in range(3):
                for c in range(3):
                    char = board[row + r][col + c]
                    if char != ".":
                        if char in unique_numbers:
                            return False
                        else:
                            unique_numbers.add(char)
            return True

        for row in range(rows):
            if not is_row_valid(row):
                return False

        for col in range(cols):
            if not is_col_valid(col):
                return False

        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                if not is_subbox_valid(row, col):
                    return False

        return True


from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: hash set, built-in data structure
        """
        rows = len(board)
        cols = len(board[0])

        row_uniq = defaultdict(set)
        col_uniq = defaultdict(set)
        box_uniq = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                element = board[row][col]

                if element != ".":
                    if (element in row_uniq[row]
                        or element in col_uniq[col]
                        or element in box_uniq[(row//3, col//3)]
                    ):
                        return False
                    else:
                        row_uniq[row].add(element)
                        col_uniq[col].add(element)
                        box_uniq[(row//3, col//3)].add(element)

        return True


print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == True)
print(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == False)
print(Solution().isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"],  ["8", ".", ".", ".", ".", ".", ".", "2", "."],  [".", ".", "2", ".", "7", ".", ".", ".", "."],  [".", "1", "5", ".", ".", ".", ".", ".", "."],  [".", ".", ".", ".", ".", "2", ".", ".", "."],  [".", "2", ".", "9", ".", ".", ".", ".", "."],  [".", ".", "4", ".", ".", ".", ".", ".", "."]]) == False)