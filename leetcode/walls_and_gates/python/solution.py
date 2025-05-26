class Solution:
    def islandsAndTreasure(self, grid: list[list[float]]) -> list[list[float]]:
        """
        Time complexity: O(n4)
            may vistit the same land more than once
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col, distance):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                grid[row][col] < distance or
                    (distance and grid[row][col] == 0)):
                return

            grid[row][col] = min(grid[row][col], distance)

            for r, c in directions:
                dfs(row + r, col + c, distance + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
                    
        return grid


from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[float]]) -> list[list[float]]:
        """
        Time complexity: O(n4)
            may vistit the same land more than once
        Auxiliary space complexity: O(n2)
        Tags: dfs, iteration, queue, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row, col, distance):
            queue = deque([(row, col, distance)])

            while queue:
                row, col, distance = queue.pop()
                grid[row][col] = min(grid[row][col], distance)

                for r, c in directions:
                    if (0 <= row + r < rows and
                        0 <= col + c < cols and
                            grid[row + r][col + c] > distance):
                        queue.append((row + r, col + c, distance + 1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row, col, 0)
                    
        return grid


print(Solution().islandsAndTreasure([[0, -1], [float("inf"), float("inf")]]) == [[0, -1], [1, 2]])
print(Solution().islandsAndTreasure([[float("inf"), float("inf"), float("inf")], [float("inf"), -1, float("inf")], [0, float("inf"), float("inf")]]) == [[2, 3, 4], [1, -1, 3], [0, 1, 2]])
print(Solution().islandsAndTreasure([[float("inf"), -1, 0, float("inf")], [float("inf"), float("inf"), float("inf"), -1], [float("inf"), -1, float("inf"), -1], [0, -1, float("inf"), float("inf")]]) == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])
