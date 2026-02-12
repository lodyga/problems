class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        ROWS = len(img)
        COLS = len(img[0])
        res = [[0] * COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                cell = 0
                divider = 0

                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if (
                            r < 0 or r > ROWS - 1 or
                            c < 0 or c > COLS - 1
                        ):
                            continue

                        cell += img[r][c]
                        divider += 1

                res[row][col] = cell // divider

        return res


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Result space complexity: O(1)
        Tags:
            A: iteration, bit manipulation, in-place method
        """
        ROWS = len(img)
        COLS = len(img[0])

        for row in range(ROWS):
            for col in range(COLS):
                cell = 0
                divider = 0

                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if (
                            r < 0 or r > ROWS - 1 or
                            c < 0 or c > COLS - 1
                        ):
                            continue

                        cell += img[r][c] & 255
                        divider += 1

                img[row][col] |= (cell // divider) << 8
            
        for row in range(ROWS):
            for col in range(COLS):
                img[row][col] >>= 8

        return img


print(Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
print(Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137], [141, 138, 141], [137, 141, 137]])
