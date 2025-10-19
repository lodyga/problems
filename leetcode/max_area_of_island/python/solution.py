from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        max_area = 0

        def bfs(row: int, col: int) -> int:
            grid[row][col] = 0
            area = 1
            queue = deque([(row, col)])

            while queue:
                row, col = queue.popleft()

                for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                    if (
                        r == -1 or r == ROWS or
                        c == -1 or c == COLS or
                        grid[r][c] == 0
                    ):
                        continue

                    queue.append((r, c))
                    grid[r][c] = 0
                    area += 1
            return area
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    max_area = max(max_area, bfs(row, col))

        return max_area


class Solution2:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, graph, matrix
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        max_area = 0

        def dfs(row: int, col: int) -> int:
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                grid[row][col] == 0
            ):
                return 0
            
            grid[row][col] = 0

            area = 1
            for r, c in DIRECTIONS:
                area += dfs(r + row, c + col)
            return area
        
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))
        
        return max_area


print(Solution().maxAreaOfIsland([[0]]) == 0)
print(Solution().maxAreaOfIsland([[1]]) == 1)
print(Solution().maxAreaOfIsland([[0, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]) == 3)
print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6)
print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0)