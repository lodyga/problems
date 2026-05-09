class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
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

        def dfs(row: int, col: int) -> int:
            if (row in (-1, ROWS) or
                col in (-1, COLS) or
                visited[row][col] or
                grid[row][col] == 0
            ):
                return 0

            visited[row][col] = True
            res = 1

            for (dr, dc) in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                res += dfs(r, c)

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] and 
                    not visited[row][col]
                ):
                    res = max(res, dfs(row, col))

        return res


class Solution:
    def maxAreaOfIsland(self, grid: list[list[str]]) -> int:
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

        def bfs(row: int, col: int) -> int:
            queue = deque([(row, col)])
            visited[row][col] = True
            res = 1

            while queue:
                row, col = queue.popleft()

                for (dr, dc) in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                
                    if (
                        r in (-1, ROWS) or
                        c in (-1, COLS) or
                        visited[r][c] or
                        grid[r][c] == 0
                    ):
                        continue

                    queue.append((r, c))
                    visited[r][c] = True
                    res += 1
                
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] and 
                    not visited[row][col]
                ):
                    res = max(res, bfs(row, col))

        return res


print(Solution().maxAreaOfIsland([[0]]) == 0)
print(Solution().maxAreaOfIsland([[1]]) == 1)
print(Solution().maxAreaOfIsland([[0, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0], [0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1)
print(Solution().maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]) == 3)
print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6)
print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0)
