class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        is_negative = False
        min_element = abs(matrix[0][0])
        total = 0

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                total += abs(matrix[row][col])
                min_element = min(min_element, abs(matrix[row][col]))
                if matrix[row][col] < 0:
                    is_negative = False if is_negative else True

        total -= min_element * 2 if is_negative else 0
        return total


print(Solution().maxMatrixSum([[1, -1], [-1, 1]]) == 4)
print(Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16)
