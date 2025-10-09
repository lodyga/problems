import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, graph, matrix
        Dijkstra's alg
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        # (height difference, min effort, x, y)
        height_heap = [(0, 0, 0, 0)]

        def bfs():
            while height_heap:
                _, min_effort, row, col = heapq.heappop(height_heap)
                if (row, col) == (ROWS - 1, COLS - 1):
                    return min_effort
                elif (row, col) in visited:
                    continue
                visited[row][col] = True

                for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                    if (
                        -1 < r < ROWS and
                        -1 < c < COLS and
                        not visited[r][c]
                    ):
                        height_difference = abs(heights[r][c] - heights[row][col])
                        new_effort = max(min_effort, height_difference)
                        heapq.heappush(
                            height_heap, 
                            (height_difference, new_effort, r, c))

        return bfs()


print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2)
print(Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1)
print(Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0)
print(Solution().minimumEffortPath([[10, 8], [10, 8], [1, 2], [10, 3], [1, 3], [6, 3], [5, 2]]) == 6)