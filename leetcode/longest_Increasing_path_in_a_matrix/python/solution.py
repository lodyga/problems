class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-down
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        # memoization for longest increating path values
        # memo[row][col] = lip value
        memo = [[-1] * COLS for _ in range(ROWS)]

        def dfs(row, col, prev):
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                matrix[row][col] <= prev
            ):
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]

            lis = 0
            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                lis = max(lis, 1 + dfs(r, c, matrix[row][col]))

            memo[row][col] = lis
            return lis

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, -1)

        lis = 1
        for row in range(ROWS):
            for col in range(COLS):
                lis = max(lis, memo[row][col])

        return lis


print(Solution().longestIncreasingPath([[1]]) == 1)
print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4)
print(Solution().longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4)
print(Solution().longestIncreasingPath([[5, 5, 3], [2, 3, 6], [1, 1, 1]]) == 4)
print(Solution().longestIncreasingPath([[1, 2, 3], [2, 1, 4], [7, 6, 5]]) == 7)
print(Solution().longestIncreasingPath([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [119, 118, 117, 116, 115, 114, 113, 112, 111, 110], [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [139, 138, 137, 136, 135, 134, 133, 132, 131, 130], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 140)
