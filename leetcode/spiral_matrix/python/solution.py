class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        spiral = []
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while True:
            for index in range(left, right + 1):
                spiral.append(matrix[top][index])
            if top == bottom:
                break
            top += 1
            
            for index in range(top, bottom + 1):
                spiral.append(matrix[index][right])
            if left == right:
                break
            right -= 1
            
            for index in reversed(range(left, right + 1)):
                spiral.append(matrix[bottom][index])
            if top == bottom:
                break
            bottom -= 1

            for index in reversed(range(top, bottom + 1)):
                spiral.append(matrix[index][left])
            if left == right:
                break
            left += 1

        return spiral


print(Solution().spiralOrder([[4, 5, 6]]) == [4, 5, 6])
print(Solution().spiralOrder([[7], [9], [6]]) == [7, 9, 6])
print(Solution().spiralOrder([[4, 5], [6, 7]]) == [4, 5, 7, 6])
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])