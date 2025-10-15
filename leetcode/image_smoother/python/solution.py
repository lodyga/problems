class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: iteration
        """
        ROWS = len(img)
        COLS = len(img[0])
        smoother = [[0] * COLS for _ in range(ROWS)]

        def square_mean(row, col):
            total = 0
            divider = 0

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (
                        -1 < r < ROWS and
                        -1 < c < COLS
                    ):
                        total += img[r][c]
                        divider += 1
            return total // divider

        for row in range(ROWS):
            for col in range(COLS):
                smoother[row][col] = square_mean(row, col)

        return smoother


print(Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137], [141, 138, 141], [137, 141, 137]])