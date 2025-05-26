class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        island_counter = 0
        visited_cells = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                grid[row][col] == "0" or
                    (row, col) in visited_cells):
                return 0

            visited_cells.add((row, col))
            for r, c in directions:
                dfs(row + r, col + c)
            
            return 1

        for row in range(rows):
            for col in range(cols):
                island_counter += dfs(row, col)
        
        return island_counter


from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        island_counter = 0
        visited_cells = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row, col):
            queue = deque([(row, col)])

            while queue:
                row, col = queue.pop()
                visited_cells.add((row, col))

                for r, c in directions:
                    if (0 <= row + r < rows and
                        0 <= col + c < cols and
                        grid[row + r][col + c] == "1" and
                            (row + r, col + c) not in visited_cells):
                        queue.append((row + r, col + c))
                        
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == "1" and 
                        (row, col) not in visited_cells):
                    island_counter += 1
                    bfs(row, col)
        
        return island_counter


print(Solution().numIslands([["0"]]) == 0)
print(Solution().numIslands([["1"]]) == 1)
print(Solution().numIslands([["0", "0"], ["0", "1"]]) == 1)
print(Solution().numIslands([["1", "0"], ["0", "1"]]) == 2)
print(Solution().numIslands([["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 3)
print(Solution().numIslands([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 2)
print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1)
print(Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]) == 3)