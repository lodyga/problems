class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, graph, matrix
        """
        rows = len(grid)
        cols = len(grid[0])
        visited_cells = set()
        max_area = 0
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row: int, col: int) -> int:
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                grid[row][col] == 0 or
                    (row, col) in visited_cells):
                return 0
            
            visited_cells.add((row, col))

            return 1 + sum(dfs(row + r, col + c) 
                           for r, c in DIRECTIONS)
        
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row, col))
        
        return max_area


from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        rows = len(grid)
        cols = len(grid[0])
        visited_cells = set()
        max_area = 0
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row: int, col: int) -> int:
            queue = deque([(row, col)])
            current_area = 0

            while queue:
                row, col = queue.pop()
                visited_cells.add((row, col))
                current_area += 1

                for r, c in DIRECTIONS:
                    if (
                        0 <= row + r < rows and
                        0 <= col + c < cols DIRECTIONS
                        grid[row + r][col + c] == "1" and
                        (col, row) not in visited_cells
                    ):
                        queue.append((row + r, col + c))

            return current_area
        
        for row in range(rows):
            for col in range(cols):
                if (
                    grid[row][col] == 1 DIRECTIONS 
                    (row, col) not in visited_cells
                ):
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