class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up
        """
        # if blocked exit
        if obstacleGrid[-1][-1]:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = [[0] * cols for _ in range(rows)]

        cache[rows - 1][cols - 1] = 1
        for col in reversed(range(cols - 1)):
            if obstacleGrid[rows - 1][col]:
                cache[rows - 1][col] = 0
            else:
                cache[rows - 1][col] = cache[rows - 1][col + 1]
        for row in reversed(range(rows - 1)):
            if obstacleGrid[row][cols - 1]:
                cache[row][cols - 1] = 0
            else:
                cache[row][cols - 1] = cache[row + 1][cols - 1]

        for row in reversed(range(rows - 1)):
            for col in reversed(range(cols - 1)):
                if obstacleGrid[row][col]:
                    cache[row][col] = 0
                else:
                    cache[row][col] = cache[row + 1][col] + cache[row][col + 1]
        
        return cache[0][0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # if blocked exit
        if obstacleGrid[-1][-1]:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = [0] * cols

        cache[-1] = 1
        for col in reversed(range(cols - 1)):
            if obstacleGrid[rows - 1][col]:
                cache[col] = 0
            else:
                cache[col] = cache[col + 1]
        
        for row in reversed(range(rows - 1)):
            if obstacleGrid[row][cols - 1]:
                cache[-1] = 0
            for col in reversed(range(cols - 1)):
                if obstacleGrid[row][col]:
                    cache[col] = 0
                else:
                    cache[col] = cache[col] + cache[col + 1]
        
        return cache[0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down
        """
        # if blocked exit or entrance
        if (
            obstacleGrid[-1][-1] or 
            obstacleGrid[0][0]
        ):
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = [[None] * cols for _ in range(rows)]
        memo[-1][-1] = 1

        def dfs(row, col):
            if (
                row == rows or
                col == cols or
                obstacleGrid[row][col]
            ):
                return 0
            elif memo[row][col] is not None:
                return memo[row][col]
            else:
                memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
                return memo[row][col]

        return dfs(0, 0)


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
print(Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]), 0)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 1, 0]]), 3)
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]), 3)