from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
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

        def dfs(row: int, col: int) -> int:
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                grid[row][col] == 0 or
                visited[row][col]
            ):
                return 0

            visited[row][col] = True

            area = 1
            for dr, dc in DIRECTIONS:
                area += dfs(row + dr, col + dc)
            return area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))
        return max_area


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
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

        def bfs(row: int, col: int) -> int:
            if (
                grid[row][col] == 0 or
                visited[row][col]
            ):
                return 0

            queue = deque([(row, col)])
            visited[row][col] = True
            area = 1

            while queue:
                (row, col) = queue.popleft()

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                    if (
                        r == -1 or
                        c == -1 or
                        r == ROWS or
                        c == COLS or
                        grid[r][c] == 0 or
                        visited[r][c]
                    ):
                        continue
                    queue.append((r, c))
                    visited[r][c] = True
                    area += 1

            return area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, bfs(row, col))
        return max_area


print(Solution().maxAreaOfIsland([[0]]) == 0)
print(Solution().maxAreaOfIsland([[1]]) == 1)
print(Solution().maxAreaOfIsland([[0, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]) == 3)
print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6)
print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0)
