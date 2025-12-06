class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down 
        """
        memo = [[-1] * COLS for _ in range(ROWS)]
        memo[ROWS - 1][COLS - 1] = 1

        def dfs(row, col):
            if row == ROWS or col == COLS:
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[row][col]

        return dfs(0, 0)


class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [[0] * (COLS + 1) for _ in range(ROWS)]
        for col in range(COLS):
            cache[-1][col] = 1

        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS - 1, -1, -1):
                cache[row][col] = cache[row + 1][col] + cache[row][col + 1]

        return cache[0][0]


class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [1] * (COLS + 1)
        cache[-1] = 0

        for _ in range(ROWS - 2, -1, -1):
            for col in range(COLS - 1, -1, -1):
                cache[col] += cache[col + 1]

        return cache[0]


print(Solution().uniquePaths(2, 1) == 1)
print(Solution().uniquePaths(1, 2) == 1)
print(Solution().uniquePaths(2, 2) == 2)
print(Solution().uniquePaths(2, 3) == 3)
print(Solution().uniquePaths(3, 2) == 3)
print(Solution().uniquePaths(3, 7) == 28)
