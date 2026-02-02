import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, array (matrix)
            A: greedy, Dijkstra
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        # heap((water level, row, col), )
        water_heap = [(grid[0][0], 0, 0)]
        highest_water_level = grid[0][0]
        visited[0][0] = True

        while water_heap:
            water_level, row, col = heapq.heappop(water_heap)
            highest_water_level = max(highest_water_level, water_level)

            if (row, col) == (ROWS - 1, COLS - 1):
                return highest_water_level

            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc

                if (
                    r == -1 or r == ROWS or
                    c == -1 or c == COLS or
                    visited[r][c]
                ):
                    continue

                heapq.heappush(water_heap, (grid[r][c], r, c))
                visited[r][c] = True


print(Solution().swimInWater([[0, 2], [1, 3]]) == 3)
print(Solution().swimInWater([[3, 2], [0, 1]]) == 3)
print(Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16)
