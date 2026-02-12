class Solution:
    def trapRainWater(self, height_map: list[list[int]]) -> int:
        import heapq
        """
        Time complexity: O(n2log(n2))
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, array (matrix)
            A: greedy, multi-source Dijkstra
        """
        ROWS = len(height_map)
        COLS = len(height_map[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        # heap([(height, row, col), ])
        height_heap = []

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    row in (0, ROWS - 1) or
                    col in (0, COLS - 1)
                ):
                    height = height_map[row][col]
                    heapq.heappush(height_heap, (height, row, col))
                    visited[row][col] = True

        def dijkstra():
            max_height = 0
            res = 0

            while height_heap:
                height, row, col = heapq.heappop(height_heap)
                max_height = max(max_height, height)
                res += max_height - height

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or r == ROWS or
                        c == -1 or c == COLS or
                        visited[r][c]
                    ):
                        continue

                    heapq.heappush(height_heap, (height_map[r][c], r, c))
                    visited[r][c] = True

            return res

        return dijkstra()


print(Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]) == 4)
print(Solution().trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) == 10)
print(Solution().trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]) == 14)
