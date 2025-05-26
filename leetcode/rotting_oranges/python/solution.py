from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.fresh_counter = 0
        self.max_distance = 0

        def bfs(queue):
            distance = 0
            while queue and self.fresh_counter:
                distance += 1
                for _ in range(len(queue)):
                    row, col, distance = queue.popleft()
                    if grid[row][col] == float("inf"):
                        self.fresh_counter -= 1
                    grid[row][col] = min(grid[row][col], distance)
                    self.max_distance = max(self.max_distance, grid[row][col])

                    for r, c in directions:
                        if (0 <= row + r < rows and
                            0 <= col + c < cols and
                                grid[row + r][col + c] > distance):
                            queue.append((row + r, col + c, distance + 1))

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    # queue rotten oranges and treat those cells as water
                    queue.append((row, col, 0))
                    grid[row][col] = 0

                if grid[row][col] == 1:
                    # change fresh oranges from 1 to inf
                    grid[row][col] = float("inf")
                    self.fresh_counter += 1

        # no fresh oranges
        if self.fresh_counter == 0:
            return 0

        bfs(queue)
        # if at least one unreachable orange exists
        if self.fresh_counter:
            return -1
        else:
            return self.max_distance


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n4)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = [[float("inf")] * cols for _ in range(rows)]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()

        def dfs(row, col, distance):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                grid[row][col] == 0 or
                grid_copy[row][col] <= distance or
                    (row, col) in visited_cells):
                return

            grid_copy[row][col] = min(grid_copy[row][col], distance)
            visited_cells.add((row, col))

            for r, c in directions:
                dfs(row + r, col + c, distance + 1)

            visited_cells.remove((row, col))

        # replace water 0 wtith -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    grid_copy[row][col] = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    dfs(row, col, 0)

        # if at least one unreachable orange exists
        if any(float("inf") in row for row in grid_copy):
            return -1
        else:
            ans = max(max(row) for row in grid_copy)
            # only water cells
            return 0 if ans == -1 else ans


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4)
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1)
print(Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2)
print(Solution().orangesRotting([[0, 2]]) == 0)
print(Solution().orangesRotting([[0]]) == 0)
print(Solution().orangesRotting([[0, 0, 2, 1, 0, 1], [1, 2, 1, 1, 2, 1], [2, 1, 2, 2, 2, 0], [2, 2, 1, 0, 0, 2], [2, 2, 1, 0, 2, 2], [2, 1, 1, 2, 2, 0], [2, 2, 1, 0, 1, 1], [2, 1, 2, 1, 0, 1], [2, 1, 2, 2, 2, 2]]) == 2)
