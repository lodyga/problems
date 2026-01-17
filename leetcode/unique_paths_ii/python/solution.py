class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: top-down
        """
        # if exit or entrance is blocked
        if (
            obstacle_grid[-1][-1] or 
            obstacle_grid[0][0]
        ):
            return 0
        
        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        memo[-1][-1] = 1

        def dfs(row: int, col: int) -> int:
            if (
                row == ROWS or
                col == COLS or
                obstacle_grid[row][col]
            ):
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]

            right = dfs(row, col + 1)
            down = dfs(row + 1, col)
            memo[row][col] = right + down
            return memo[row][col]

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
        # if exit or entrance is blocked
        if (
            obstacle_grid[-1][-1] or 
            obstacle_grid[0][0]
        ):
            return 0
        
        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[-1][-2] = 1

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if obstacle_grid[row][col]:
                    continue
                
                right = cache[row][col + 1]
                down = cache[row + 1][col]
                cache[row][col] = right + down

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
        # if exit or entrance is blocked
        if (
            obstacle_grid[-1][-1] or 
            obstacle_grid[0][0]
        ):
            return 0
        
        ROWS = len(obstacle_grid)
        COLS = len(obstacle_grid[0])
        next_cache = [0] * (COLS + 1)
        next_cache[-2] = 1

        for row in range(ROWS - 1, -1, -1):
            cache = [0] * (COLS + 1)
            for col in range(COLS - 1, -1, -1):
                if obstacle_grid[row][col]:
                    continue
                
                right = cache[col + 1]
                down = next_cache[col]
                cache[col] = right + down
            
            next_cache = cache

        return next_cache[0]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2)
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1)
print(Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == 3)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]) == 3)
