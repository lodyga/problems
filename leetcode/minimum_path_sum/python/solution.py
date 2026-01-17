class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-dwon
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        memo[-1][-1] = grid[ROWS - 1][COLS - 1]
        UPPER_BOUND = 10**7

        def dfs(row, col):
            if (row == ROWS or col == COLS):
                return UPPER_BOUND
            elif memo[row][col] != -1:
                return memo[row][col]
            
            cell = grid[row][col]
            right = dfs(row, col + 1)
            down = dfs(row + 1, col)
            res = cell + min(right, down)
            memo[row][col] = res
            return res

        return dfs(0, 0)


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        UPPER_BOUND = 10**7
        cache = [[UPPER_BOUND] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[-1][-2] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                cell = grid[row][col]
                right = cache[row][col + 1]
                down = cache[row + 1][col]
                cache[row][col] = cell + min(right, down)

        return cache[0][0]


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        UPPER_BOUND = 10**7
        next_cache = [UPPER_BOUND] * (COLS + 1)
        next_cache[-2] = 0

        for row in range(ROWS - 1, -1, -1):
            cache = [UPPER_BOUND] * (COLS + 1)
            for col in range(COLS - 1, -1, -1):
                cell = grid[row][col]
                right = cache[col + 1]
                down = next_cache[col]
                cache[col] = cell + min(right, down)
            next_cache = cache

        return next_cache[0]


print(Solution().minPathSum([[1, 2], [3, 4]]) == 7)
print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) == 12)
