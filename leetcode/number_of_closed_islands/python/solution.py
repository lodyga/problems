class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, matrix, graph
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col):
            if (
                row == -1 or
                row == ROWS or
                col == -1 or
                col == COLS
            ):
                return False
            elif grid[row][col] == 1:
                return True

            grid[row][col] = 1

            is_closed_island = True
            for r, c in ((row + r, col + c) for r, c in DIRECTIONS):
                if dfs(r, c) == False:
                    is_closed_island = False

            return is_closed_island

        counter = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    counter += dfs(row, col)

        return counter


from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row, col):
            queue = deque([(row, col)])
            is_closed_island = True

            while queue:
                row, col = queue.popleft()
                grid[row][col] = 1

                for r, c in ((row + r, col + c) for r, c in DIRECTIONS):
                    if (
                        r == -1 or
                        r == ROWS or
                        c == -1 or
                        c == COLS
                    ):
                        is_closed_island = False
                    elif grid[r][c] == 0:
                        queue.append((r, c))
                        grid[r][c] = 1

            return is_closed_island

        counter = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    counter += bfs(row, col)

        return counter


print(Solution().closedIsland([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 1)
print(Solution().closedIsland([[0, 1], [1, 1]]) == 0)
print(Solution().closedIsland([[1, 1, 1], [0, 0, 1], [1, 1, 1]]) == 0)
print(Solution().closedIsland([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 1)
print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) == 2)
print(Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1)
print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 2)
print(Solution().closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 5)