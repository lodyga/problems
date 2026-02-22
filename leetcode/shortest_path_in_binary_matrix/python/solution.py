class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        from collections import deque
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), queue
            A: bfs, iteration
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        dist = 1

        # bfs
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if (row, col) == (ROWS - 1, COLS - 1):
                    return dist

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or r == ROWS or
                        c == -1 or c == COLS or
                        visited[r][c] or
                        grid[r][c] == 1
                    ):
                        continue

                    queue.append((r, c))
                    visited[r][c] = True

            dist += 1

        return -1


print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2)
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]) == -1)
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4)
print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1)
