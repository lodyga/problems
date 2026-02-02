import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, array (matrix)
            A: greedy, Dijkstra
            Model: graph
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        def bfs(row: int, col: int) -> int:
            # heap((min effort in current path, row, col), )
            min_effort_heap = [(0, row, col)]

            while min_effort_heap:
                min_effort, row, col = heapq.heappop(min_effort_heap)
                
                if visited[row][col]:
                    continue
                visited[row][col] = True
                
                if (row, col) == (ROWS - 1, COLS - 1):
                    return min_effort

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or r == ROWS or
                        c == -1 or c == COLS or
                        visited[r][c]
                    ):
                        continue

                    height_diff = abs(heights[row][col] - heights[r][c])
                    next_min_effort = max(min_effort, height_diff)
                    heapq.heappush(min_effort_heap, (next_min_effort, r, c))

        return bfs(0, 0)


print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2)
print(Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1)
print(Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0)
print(Solution().minimumEffortPath([[10, 8], [10, 8], [1, 2], [10, 3], [1, 3], [6, 3], [5, 2]]) == 6)
