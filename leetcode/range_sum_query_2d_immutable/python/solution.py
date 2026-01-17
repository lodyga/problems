class NumMatrix:
    """
    Time complexity: 
        constructor: O(n2)
        sumRegion: O(1)
    Auxiliary space complexity: O(n2)
    Tags:
        DS: array (matrix)
        A: prefix sum
    """

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(1, ROWS + 1):
            row_prefix = 0
            for col in range(1, COLS + 1):
                row_prefix += matrix[row - 1][col - 1]
                self.prefix[row][col] = self.prefix[row - 1][col] + row_prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            - self.prefix[row1][col2 + 1]
            + self.prefix[row1][col1]
        )


numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(2, 1, 4, 3) == 8)
print(numMatrix.sumRegion(1, 1, 2, 2) == 11)
print(numMatrix.sumRegion(1, 2, 2, 4) == 12)
