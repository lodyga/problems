class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        top = left = 0
        bottom = right = n - 1
        matrix = [[0] * n for _ in range(n)]
        number = 0

        while left < right:
            # top
            for l in range(left, right):
                number += 1
                matrix[top][l] = number
            # right
            for t in range(top, bottom):
                number += 1
                matrix[t][right] = number
            # bottom
            for r in range(right, left, -1):
                number += 1
                matrix[bottom][r] = number
            # left
            for b in range(bottom, top, -1):
                number += 1
                matrix[b][left] = number
        
            top = left = left + 1
            right = bottom = right - 1
        
        if left == right:
            number += 1
            matrix[left][right] = number

        return matrix


print(Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(Solution().generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
print(Solution().generateMatrix(1) == [[1]])