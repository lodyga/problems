class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, matrix, graph, pure functional 
        """
        rows = len(grid)
        cols = len(grid[0])
        visited_cells = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def get_perimeter(row, col):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                    grid[row][col] == 0):
                return 1
            elif (row, col) in visited_cells:
                return 0

            visited_cells.add((row, col))

            return sum(get_perimeter(row + r, col + c)
                       for r, c in directions)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    return get_perimeter(row, col)


class Solution:
    def __init__(self):
        self.perimeter = 0

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, matrix, graph, class variable
        Imperative style with side effects
        """
        rows = len(grid)
        cols = len(grid[0])
        visited_cells = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def get_perimeter(row, col):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                    grid[row][col] == 0):
                self.perimeter += 1
                return
            elif (row, col) in visited_cells:
                return

            visited_cells.add((row, col))
            
            for r, c in directions:
                get_perimeter(row + r, col + c) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    get_perimeter(row, col)
                    return self.perimeter


print(Solution().islandPerimeter([[1]]), 4)
print(Solution().islandPerimeter([[1, 0]]), 4)
print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)