from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        if grid[0][0] or grid[-1][-1]:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = (
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1))

        def bfs():
            min_path = deque([(1, 0, 0)])  # (path length, row, col)
            grid[0][0] = 1

            while min_path:
                path, row, col = min_path.popleft()

                if (row, col) == (ROWS - 1, COLS - 1):
                    return path

                for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                    if (
                        r == -1 or
                        r == ROWS or
                        c == -1 or
                        c == COLS or
                        grid[r][c]
                    ):
                        continue
                    min_path.append((path + 1, r, c))
                    grid[r][c] = 1

            return -1
        
        return bfs()


print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2)
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]) == -1)
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4)
print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1)
