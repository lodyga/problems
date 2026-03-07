class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: dfs, recursion
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * (COLS*3) for _ in range((ROWS*3))]
        counter = 0

        for row in range(ROWS):
            for col in range(COLS):
                char = grid[row][col]

                if char == "\\":
                    for i in range(3):
                        visited[row*3 + i][col*3 + i] = True

                if char == "/":
                    for i in range(3):
                        visited[row*3 + i][col*3 + (2 - i)] = True

        def dfs(row, col):
            if (
                row == -1 or row == ROWS*3 or
                col == -1 or col == COLS*3 or
                visited[row][col]
            ):
                return

            visited[row][col] = True

            for (dr, dc) in DIRECTIONS:
                dfs(row + dr, col + dc)

        for row in range(ROWS*3):
            for col in range(COLS*3):
                if not visited[row][col]:
                    dfs(row, col)
                    counter += 1

        return counter


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        from collections import deque
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
        visited = [[False] * (COLS*3) for _ in range((ROWS*3))]
        counter = 0

        for row in range(ROWS):
            for col in range(COLS):
                char = grid[row][col]

                if char == "\\":
                    for i in range(3):
                        visited[row*3 + i][col*3 + i] = True

                if char == "/":
                    for i in range(3):
                        visited[row*3 + i][col*3 + (2 - i)] = True

        def bfs(row, col):
            queue = deque([(row, col)])
            visited[row][col] = True

            while queue:
                row, col = queue.pop()

                for (dr, dc) in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or r == ROWS*3 or
                        c == -1 or c == COLS*3 or
                        visited[r][c]
                    ):
                        continue

                    queue.append((r, c))
                    visited[r][c] = True

        for row in range(ROWS*3):
            for col in range(COLS*3):
                if not visited[row][col]:
                    bfs(row, col)
                    counter += 1

        return counter


print(Solution().regionsBySlashes([" /", "/ "]) == 2)
print(Solution().regionsBySlashes([" /", "  "]) == 1)
print(Solution().regionsBySlashes(["/\\", "\\/"]) == 5)
