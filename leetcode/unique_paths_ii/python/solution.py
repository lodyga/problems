class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-down
        """
        def dfs(row: int, col: int) -> int:
            if (
                row == ROWS or col == COLS
                or obstacle_grid[row][col]
            ):
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]

            res = dfs(row + 1, col) + dfs(row, col + 1)
            memo[row][col] = res
            return res

        if (obstacle_grid[0][0] or obstacle_grid[-1][- 1]):
            return 0

        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        memo[-1][-1] = 1
        return dfs(0, 0)


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        if (obstacle_grid[0][0] or obstacle_grid[-1][- 1]):
            return 0

        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[-1][-2] = 1

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if obstacle_grid[row][col] == 0:
                    cache[row][col] = cache[row + 1][col] + cache[row][col + 1]

        return cache[0][0]


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix)
            A: bottom-up
        """
        if (obstacle_grid[0][0] or obstacle_grid[-1][- 1]):
            return 0

        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        next_cache = [0] * (COLS + 1)
        next_cache[-2] = 1

        for row in range(ROWS - 1, -1, -1):
            cache = [0] * (COLS + 1)

            for col in range(COLS - 1, -1, -1):
                if obstacle_grid[row][col] == 0:
                    cache[col] = next_cache[col] + cache[col + 1]

            next_cache = cache

        return next_cache[0]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2)
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1)
print(Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == 3)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]) == 3)
