from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[float]]) -> list[list[float]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: 
            DS: array (matrix), queue
            A: bfs, iteration
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs() -> None:
            while queue:
                (row, col, distance) = queue.popleft()

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                    if (
                        -1 < r < ROWS and
                        -1 < c < COLS and
                        grid[r][c] == float("inf")
                    ):
                        queue.append((r, c, distance + 1))
                        grid[r][c] = distance + 1

        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        bfs()
        return grid


print(Solution().islandsAndTreasure([[0, -1], [float("inf"), float("inf")]]) == [[0, -1], [1, 2]])
print(Solution().islandsAndTreasure([[float("inf"), float("inf"), float("inf")], [float("inf"), -1, float("inf")], [0, float("inf"), float("inf")]]) == [[2, 3, 4], [1, -1, 3], [0, 1, 2]])
print(Solution().islandsAndTreasure([[float("inf"), -1, 0, float("inf")], [float("inf"), float("inf"), float("inf"), -1], [float("inf"), -1, float("inf"), -1], [0, -1, float("inf"), float("inf")]]) == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])
