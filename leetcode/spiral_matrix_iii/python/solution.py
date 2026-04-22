class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = rows
        COLS = cols
        DIM = rows * cols
        # left, down, up, right
        directions = [1, 1, 2, 2]
        x = cStart
        y = rStart
        res = [[y, x]]

        while len(res) < DIM:
            for _ in range(1, directions[0] + 1):
                x += 1
                if -1 < y < ROWS and -1 < x < COLS:
                    res.append([y, x])

            for _ in range(1, directions[1] + 1):
                y += 1
                if -1 < y < ROWS and -1 < x < COLS:
                    res.append([y, x])

            for _ in range(1, directions[2] + 1):
                x -= 1
                if -1 < y < ROWS and -1 < x < COLS:
                    res.append([y, x])

            for _ in range(1, directions[3] + 1):
                y -= 1
                if -1 < y < ROWS and -1 < x < COLS:
                    res.append([y, x])

            directions = [d + 2 for d in directions]

        return res


print(Solution().spiralMatrixIII(1, 4, 0, 0) == [[0, 0], [0, 1], [0, 2], [0, 3]])
print(Solution().spiralMatrixIII(5, 6, 1, 4) == [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
print(Solution().spiralMatrixIII(3, 3, 1, 1) == [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]])
print(Solution().spiralMatrixIII(3, 3, 2, 2) == [[2, 2], [2, 1], [1, 1], [1, 2], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]])
