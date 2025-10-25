class Solution:
    def construct2DArray(self, original: list[int], ROWS: int, COLS: int) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: matrix
        """
        if len(original) != ROWS * COLS:
            return []

        matrix = [[0] * COLS for _ in range(ROWS)]

        for index in range(len(original)):
            row = index // COLS
            col = index % COLS            
            matrix[row][col] = original[index]

        return matrix


class Solution:
    def construct2DArray(self, original: list[int], ROWS: int, COLS: int) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: matrix
        """
        if len(original) != ROWS * COLS:
            return []

        matrix = [[0] * COLS for _ in range(ROWS)]
        index = 0

        for row in range(ROWS):
            for col in range(COLS):
                matrix[row][col] = original[index]
                index += 1

        return matrix


print(Solution().construct2DArray([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]])
print(Solution().construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]])
print(Solution().construct2DArray([1, 2], 1, 1) == [])