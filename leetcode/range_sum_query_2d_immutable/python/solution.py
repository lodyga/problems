class NumMatrix:
    """
    Time complexity: 
        constructor: O(n2)
        sumRegion: O(1)
    Auxiliary space complexity: O(n2)
    Tags: prefix sum
    """
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            row_prefix = 0
            for col in range(cols):
                row_prefix += matrix[row][col]
                self.prefix_matrix[row + 1][col + 1] = \
                    self.prefix_matrix[row][col + 1] \
                    + row_prefix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_matrix[row2 + 1][col2 + 1] \
            - self.prefix_matrix[row2 + 1][col1] \
            - self.prefix_matrix[row1][col2 + 1] \
            + self.prefix_matrix[row1][col1]
        )


numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
print(numMatrix.sumRegion(2, 1, 4, 3))  # return 8 (i.e sum of the red rectangle)
print(numMatrix.sumRegion(1, 1, 2, 2))  # return 11 (i.e sum of the green rectangle)
print(numMatrix.sumRegion(1, 2, 2, 4))  # return 12 (i.e sum of the blue rectangle)