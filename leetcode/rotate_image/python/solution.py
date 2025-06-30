class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        left = 0 
        right = len(matrix) - 1

        while left < right:
            top = left
            bottom = right

            for index in range(right - left):
                top_left = matrix[top][left + index]
                matrix[top][left + index] = matrix[bottom - index][left]
                matrix[bottom - index][left] = matrix[bottom][right - index]
                matrix[bottom][right - index] = matrix[top + index][right]
                matrix[top + index][right] = top_left

            left += 1
            right -= 1

        return matrix


print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
print(Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])


import numpy as np
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix = np.rot90(matrix, -1, (0, 1))
        return matrix