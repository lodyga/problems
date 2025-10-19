from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        
        grid_sum = sum(number for row in grid for number in row)
        if (
            grid_sum == 0 or 
            grid_sum == ROWS * COLS
        ):
            return -1

        # if all(all(row) for row in grid):
        #     return -1
        # if not any(any(row) for row in grid):
        #     return -1

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        self.last_distance = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    queue.append((row, col))
                    grid[row][col] = -1

        def bfs():
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    self.last_distance = distance

                    for (r, c) in ((r + row, c + col) for r, c in DIRECTIONS):
                        if (
                           r == -1 or
                           r == ROWS or
                           c == -1 or
                           c == COLS or
                           grid[r][c] != 0
                        ):
                            continue

                        queue.append((r, c))
                        grid[r][c] = distance + 1

                distance += 1
            
        bfs()
        return self.last_distance


import heapq

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, graph, matrix
        Dijkstra's alg
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        if all(number == 0 for row in grid for number in row):
            return -1
        if all(number == 1 for row in grid for number in row):
            return -1

        if all(all(row) for row in grid):
            return -1
        if not any(any(row) for row in grid):
            return -1

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        distance_heap = []
        self.last_distance = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    heapq.heappush(distance_heap, (0, row, col))
                    grid[row][col] = -1


        def bfs():
            while distance_heap:
                distance, row, col = heapq.heappop(distance_heap)
                self.last_distance = distance

                for (r, c) in ((r + row, c + col) for r, c in DIRECTIONS):
                    if (
                       r == -1 or
                       r == ROWS or
                       c == -1 or
                       c == COLS or
                       grid[r][c] != 0
                    ):
                        continue

                    heapq.heappush(distance_heap, (distance + 1, r, c))
                    grid[r][c] = distance + 1
                
        bfs()
        return self.last_distance


print(Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2)
print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4)
print(Solution().maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == -1)
print(Solution().maxDistance([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == -1)