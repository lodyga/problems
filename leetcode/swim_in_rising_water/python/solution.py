import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, graph, matrix
        Dijkstra's alg
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        water_heap = [(grid[0][0], 0, 0)]  # min water level cell
        visited = [[False] * COLS for _ in range(ROWS)]
        visited[0][0] = True

        # bfs()
        while water_heap:
            water_level, row, col = heapq.heappop(water_heap)

            if (row, col) == (ROWS - 1, COLS - 1):
                return water_level
            
            for r, c in DIRECTIONS:
                side_row = row + r
                side_col = col + c
                if (
                    -1 < side_row < ROWS and
                    -1 < side_col < COLS and
                    not visited[side_row][side_col]
                ):
                    reachable_water_level = max(water_level, grid[side_row][side_col])
                    heapq.heappush(water_heap, (reachable_water_level, side_row, side_col))
                    visited[side_row][side_col] = True


print(Solution().swimInWater([[0, 2], [1, 3]]) == 3)
print(Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16)
print(Solution().swimInWater([[3, 2], [0, 1]]) == 3)