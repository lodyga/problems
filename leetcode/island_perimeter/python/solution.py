from collections import deque


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (row + dr, col + dc)

                        if (
                            r in (-1, ROWS)
                            or c in (-1, COLS)
                            or grid[r][c] == 0
                        ):
                            res += 1


        return res


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
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

        def dfs(row, col):
            if (
                row in (-1, ROWS)
                or col in (-1, COLS)
                or grid[row][col] == 0
            ):
                return 1
            elif visited[row][col]:
                return 0

            res = 0
            visited[row][col] = True

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                res += dfs(r, c)

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return dfs(row, col)
        return 0


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
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
        visited = [[False] * COLS for _ in range(ROWS)]

        def bfs(row, col):
            res = 0
            queue = deque([(row, col)])
            visited[row][col] = True

            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r in (-1, ROWS)
                        or c in (-1, COLS)
                        or grid[r][c] == 0
                    ):
                        res += 1

                    elif grid[r][c] == 1 and not visited[r][c]:
                        queue.append((r, c))
                        visited[r][c] = True

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return bfs(row, col)

        return 0


print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16)
print(Solution().islandPerimeter([[1]]) == 4)
print(Solution().islandPerimeter([[1, 0]]) == 4)
print(Solution().islandPerimeter([[0]]) == 0)
print(Solution().islandPerimeter([[1, 1], [1, 1]]) == 8)
