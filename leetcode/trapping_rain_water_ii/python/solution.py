import heapq


class Solution:
    def trapRainWater(self, height_map: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, graph
        Dijkstra's alg
        """
        ROWS = len(height_map)
        COLS = len(height_map[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height_heap = []

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    row == 0 or
                    row == ROWS - 1 or
                    col == 0 or
                    col == COLS - 1
                ):
                    heapq.heappush(height_heap, (height_map[row][col], row, col))
                    height_map[row][col] = -1

        def bfs():
            max_height = 0
            trapped_water = 0

            while height_heap:
                height, row, col = heapq.heappop(height_heap)
                max_height = max(max_height, height)
                trapped_water += max_height - height

                for nr, nc in ((r + row, c + col) for r, c in DIRECTIONS):
                    if (
                        nr == -1 or
                        nr == ROWS or
                        nc == -1 or
                        nc == COLS or
                        height_map[nr][nc] == -1
                    ):
                        continue

                    heapq.heappush(height_heap, (height_map[nr][nc], nr, nc))
                    height_map[nr][nc] = -1
            
            return trapped_water

        return bfs()


print(Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]) == 4)
print(Solution().trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) == 10)
print(Solution().trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]) == 14)


class Solution:
    def trapRainWater(self, height_map: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        failed
        """
        ROWS = len(height_map)
        COLS = len(height_map[0])
        trapped_water = 0

        # Calculate by 3 rows
        for row in range(ROWS - 2):
            left = 0
            right = COLS - 1
            max_left_height = [height_map[row][left] for row in range(row, row + 3)]
            max_right_height = [height_map[row][right] for row in range(row, row + 3)]

            while left <= right:
                left_height = [height_map[row][left] for row in range(row, row + 3)]
                right_height = [height_map[row][right] for row in range(row, row + 3)]
                
                if left_height < right_height:
                    max_left_height = [max(max_left_height[k], left_height[k]) for k in range(3)]
                    min_surround = min(max_left_height)
                    cell_height = height_map[row + 1][left]
                    if min_surround > cell_height:
                        trapped_water += min_surround - cell_height
                    left += 1
                else:
                    max_right_height = [max(max_right_height[k], right_height[k]) for k in range(3)]
                    min_surround = min(max_right_height)
                    cell_height = height_map[row + 1][right]
                    if min_surround > cell_height:
                        trapped_water += min_surround - cell_height
                    right -= 1

        return trapped_water