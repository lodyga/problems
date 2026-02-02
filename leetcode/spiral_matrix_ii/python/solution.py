class Solution:
    def generateMatrix(self, N: int) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        left = top = 0
        right = bottom = N - 1
        res = [[1] * N for _ in range(N)]
        num = 1

        while left < right:

            # fill top row
            for l in range(left, right):
                res[top][l] = num
                num += 1

            # fill right column
            for t in range(top, bottom):
                res[t][right] = num
                num += 1

            # fill bottom row
            for r in range(right, left, -1):
                res[bottom][r] = num
                num += 1

            # fill left column
            for b in range(bottom, top, -1):
                res[b][left] = num
                num += 1

            left += 1
            top += 1
            right -= 1
            bottom -= 1

            if left == right:
                res[top][left] = num
                break

        return res


print(Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(Solution().generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
print(Solution().generateMatrix(1) == [[1]])
