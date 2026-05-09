class Solution:
    def islandsAndTreasure(self, grid: list[list[float]]) -> list[list[float]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), queue
            A: multi-source BFS
        """
        from collections import deque
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()

        def bfs() -> None:
            distance = 0
            
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    
                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (row + dr, col + dc)

                        if (
                            r in (-1, ROWS) or
                            c in (-1, COLS) or
                            grid[r][c] <= grid[row][col]
                        ):
                            continue

                        queue.append((r, c))
                        grid[r][c] = distance + 1

                distance += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        bfs()
        return grid


print(Solution().islandsAndTreasure([[0, -1], [2147483647, 2147483647]]) == [[0, -1], [1, 2]])
print(Solution().islandsAndTreasure([[2147483647, 2147483647, 2147483647], [2147483647, -1, 2147483647], [0, 2147483647, 2147483647]]) == [[2, 3, 4], [1, -1, 3], [0, 1, 2]])
print(Solution().islandsAndTreasure([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]) == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])
