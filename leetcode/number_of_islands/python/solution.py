class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
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
        visited = [[False] * COLS for _ in range(ROWS)]
        res = 0

        def dfs(row: int, col: int) -> None:
            if (row in (-1, ROWS) or
                col in (-1, COLS) or
                visited[row][col] or
                grid[row][col] == "0"
            ):
                return

            visited[row][col] = True

            for (dr, dc) in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                dfs(r, c)

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] == "1" and 
                    not visited[row][col]
                ):
                    dfs(row, col)
                    res += 1

        return res


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), queue
            A: bfs, iteration
        """
        from collections import deque
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        res = 0

        def bfs(row: int, col: int) -> None:
            queue = deque([(row, col)])
            visited[row][col] = True

            while queue:
                row, col = queue.popleft()

                for (dr, dc) in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                
                    if (
                        r in (-1, ROWS) or
                        c in (-1, COLS) or
                        visited[r][c] or
                        grid[r][c] == "0"
                    ):
                        continue

                    queue.append((r, c))
                    visited[r][c] = True

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] == "1" and 
                    not visited[row][col]
                ):
                    bfs(row, col)
                    res += 1

        return res


print(Solution().numIslands([["0"]]) == 0)
print(Solution().numIslands([["1"]]) == 1)
print(Solution().numIslands([["0", "0"], ["0", "1"]]) == 1)
print(Solution().numIslands([["1", "0"], ["0", "1"]]) == 2)
print(Solution().numIslands([["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 3)
print(Solution().numIslands([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 2)
print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1)
print(Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]) == 3)
