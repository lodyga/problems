class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        is_positive = True
        total = 0
        min_val = abs(matrix[0][0])

        for row in range(ROWS):
            for col in range(COLS):
                total += abs(matrix[row][col])

                if matrix[row][col] < 0:
                    is_positive = not is_positive

                if abs(matrix[row][col]) < min_val:
                    min_val = abs(matrix[row][col])

        return total if is_positive else total - 2*min_val


print(Solution().maxMatrixSum([[1, -1], [-1, 1]]) == 4)
print(Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16)
