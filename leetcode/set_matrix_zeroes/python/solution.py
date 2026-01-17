class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_mark = [False] * ROWS
        col_mark = [False] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_mark[row] = True
                    col_mark[col] = True

        for row in range(ROWS):
            for col in range(COLS):
                if row_mark[row] or col_mark[col]:
                    matrix[row][col] = 0

        return matrix


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        first_row_is_zero = False
        first_col_is_zero = False

        # Mark if the first column is zero.
        for row in range(ROWS):
            if matrix[row][0] == 0:
                first_col_is_zero = True
                break

        # Mark if the first row is zero.
        for col in range(COLS):
            if matrix[0][col] == 0:
                first_row_is_zero = True
                break

        # Mark 'zero' rows in the first column and
        # 'zero' columns in the first row.
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Zero out the matrix except the first colums and row.
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if (
                    matrix[row][0] == 0 or
                    matrix[0][col] == 0
                ):
                    matrix[row][col] = 0

        if first_col_is_zero:
            for row in range(ROWS):
                matrix[row][0] = 0

        if first_row_is_zero:
            for col in range(COLS):
                matrix[0][col] = 0

        return matrix


print(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
print(Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]) == [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
