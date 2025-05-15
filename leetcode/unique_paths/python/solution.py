class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        """
        Time complexity: O(m*n)
            m: number of rows
            n: number of coulmns
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        current_row = [1] * cols  # cache

        for _ in range(rows - 1):
            for col in reversed(range(cols - 1)):
                current_row[col] = current_row[col + 1] + current_row[col]

        return current_row[0]


class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        """
        Time complexity: O(m*n)
            m: number of rows
            n: number of coulmns
        Auxiliary space complexity: O(m*n)
        Tags: dp, top-down with memoization as list
        """
        memo = [[1] * cols for _ in range(rows)]

        def dfs(row, col):
            if row == rows - 1 or col == cols - 1:
                pass
            else:
                memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[row][col]

        return dfs(0, 0)


print(Solution().uniquePaths(1, 2), 1)
print(Solution().uniquePaths(2, 3), 3)
print(Solution().uniquePaths(3, 2), 3)
print(Solution().uniquePaths(3, 7), 28)