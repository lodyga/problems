class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        transpoted = [[0] * ROWS for _ in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                transpoted[col][row] = matrix[row][col]

        return transpoted


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        return [[matrix[row][col] 
                for row in range(ROWS)] 
                for col in range(COLS)]


print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
print(Solution().transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]])
