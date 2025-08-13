class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        rows = n
        cols = n
        self.counter = 0
        visited_cols = set()
        visited_diags = set()  # set(row + col, ...)
        visited_adiags = set()  # set(row - col, ...)

        def dfs(row):
            if row == rows:
                self.counter += 1
                return

            for col in range(cols):
                if (
                    col in visited_cols or
                    row + col in visited_diags or
                    row - col in visited_adiags
                ):
                    continue

                visited_cols.add(col)
                visited_diags.add(row + col)
                visited_adiags.add(row - col)
                dfs(row + 1)
                visited_cols.remove(col)
                visited_diags.remove(row + col)
                visited_adiags.remove(row - col)

        dfs(0)
        return self.counter


print(Solution().totalNQueens(1) == 1)
print(Solution().totalNQueens(2) == 0)
print(Solution().totalNQueens(3) == 0)
print(Solution().totalNQueens(4) == 2)
print(Solution().totalNQueens(5) == 10)