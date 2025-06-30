class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = [False] * rows
        zero_cols = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows[row] = True
                    zero_cols[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if (zero_rows[row] or zero_cols[col]):
                    matrix[row][col] = 0

        return matrix


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_first_row = False

        # Mark 'zero' rows and colums. 
        # First row is marked in 'zero_first_row' because it overlaps with first column.
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        zero_first_row = True
                    else:
                        matrix[row][0] = 0
        
        # zero out the mathix except the first colums and row
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # zero out the first coulmn
        if matrix[0][0] == 0:
            for row in range(1, rows):
                matrix[row][0] = 0
        
        # zero out the first row
        if zero_first_row:
            for col in range(cols):
                matrix[0][col] = 0

        return matrix


print(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
print(Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]) == [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])