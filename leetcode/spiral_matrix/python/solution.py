class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        res = []
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while True:
            # top
            for idx in range(left, right + 1):
                res.append(matrix[top][idx])
            top += 1
            if top > bottom:
                break

            # right
            for idx in range(top, bottom + 1):
                res.append(matrix[idx][right])
            right -= 1
            if left > right:
                break

            # bottom
            for idx in range(right, left - 1, -1):
                res.append(matrix[bottom][idx])
            bottom -= 1
            if top > bottom:
                break

            # left
            for idx in range(bottom, top - 1, -1):
                res.append(matrix[idx][left])
            left += 1
            if left > right:
                break

        return res


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
print(Solution().spiralOrder([[4, 5, 6]]) == [4, 5, 6])
print(Solution().spiralOrder([[7], [9], [6]]) == [7, 9, 6])
print(Solution().spiralOrder([[4, 5], [6, 7]]) == [4, 5, 7, 6])
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]) == [1, 2, 3, 4, 8, 12, 16, 20, 24, 23, 22, 21, 17, 13, 9, 5, 6, 7, 11, 15, 19, 18, 14, 10])
