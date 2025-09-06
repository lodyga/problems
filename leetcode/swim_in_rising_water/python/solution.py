import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, matrix, graph
        Dijkstra's alg
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        path = [(grid[0][0], 0, 0)]  # height, row, col
        visited = [[False] * COLS for _ in range(ROWS)]
        min_height = 0

        while path:
            height, row, col = heapq.heappop(path)
            min_height = max(min_height, height)

            if (row, col) == (ROWS - 1, COLS - 1):
                return min_height
            
            for r, c in DIRECTIONS:
                if (
                    0 <= row + r < ROWS and
                    0 <= col + c < COLS and
                    not visited[row + r][col + c]
                ):
                    heapq.heappush(path, (grid[row + r][col + c], row + r, col + c))
                    visited[row][col] = True


print(Solution().swimInWater([[0, 2], [1, 3]]) == 3)
print(Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16)
print(Solution().swimInWater([[3, 2], [0, 1]]) == 3)