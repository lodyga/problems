class Solution:
    def construct2DArray(self, original: list[int], ROWS: int, COLS: int) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        if (len(original) != ROWS * COLS):
            return []

        res = [[0]*COLS for _ in range(ROWS)]

        for index, num in enumerate(original):
            row = index // COLS
            col = index % COLS
            res[row][col] = num

        return res


class Solution:
    def construct2DArray(self, original: list[int], ROWS: int, COLS: int) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        if (len(original) != ROWS * COLS):
            return []

        res = [[0]*COLS for _ in range(ROWS)]
        index = 0

        for row in range(ROWS):
            for col in range(COLS):
                res[row][col] = original[index]
                index += 1

        return res


print(Solution().construct2DArray([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]])
print(Solution().construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]])
print(Solution().construct2DArray([1, 2], 1, 1) == [])
