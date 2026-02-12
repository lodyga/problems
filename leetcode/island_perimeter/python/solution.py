from collections import deque


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: dfs, recursion
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(row, col):
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                grid[row][col] == 0
            ):
                return 1
            elif visited[row][col]:
                return 0

            perimeter = 0
            visited[row][col] = True

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                perimeter += dfs(r, c)

            return perimeter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return dfs(row, col)
        return 0


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), queue
            A: bfs, iteration
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        def bfs(row, col):
            perimeter = 0
            queue = deque([(row, col)])
            visited[row][col] = True

            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or
                        c == -1 or
                        r == ROWS or
                        c == COLS or
                        grid[r][c] == 0
                    ):
                        perimeter += 1
                    
                    elif grid[r][c] == 1 and not visited[r][c]:
                        queue.append((r, c))
                        visited[r][c] = True

            return perimeter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return bfs(row, col)
        return 0


print(Solution().islandPerimeter([[0]]) == 0)
print(Solution().islandPerimeter([[1]]) == 4)
print(Solution().islandPerimeter([[1, 0]]) == 4)
print(Solution().islandPerimeter([[1, 1], [1, 1]]) == 8)
print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16)
