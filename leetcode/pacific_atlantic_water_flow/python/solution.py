class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
            n: heights length
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: multi-source DFS
        """
        def dfs(
                row: int,
                col: int,
                prev_height: int,
                to_ocean: list[list[bool]]
        ) -> None:
            if (
                row in (-1, ROWS)
                or col in (-1, COLS)
                or heights[row][col] < prev_height
                or to_ocean[row][col]
            ):
                return

            to_ocean[row][col] = True

            for dr, dc in DIRECTIONS:
                dfs(row + dr, col + dc, heights[row][col], to_ocean)

        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_pacific = [[False] * COLS for _ in range(ROWS)]
        to_atlantic = [[False] * COLS for _ in range(ROWS)]
        res = []

        for row in range(ROWS):
            dfs(row, 0, 0, to_pacific)
            dfs(row, COLS - 1, 0, to_atlantic)

        for col in range(COLS):
            dfs(0, col, 0, to_pacific)
            dfs(ROWS - 1, col, 0, to_atlantic)

        for row in range(ROWS):
            for col in range(COLS):
                if to_pacific[row][col] and to_atlantic[row][col]:
                    res.append([row, col])

        return res


from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
            n: heights length
        Auxiliary space complexity: O(n2)
        Tags:
            DS: queue, array (matrix)
            A: multi-source BFS
        """
        def bfs(queue, to_ocean) -> list[list[bool]]:
            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc

                    if (
                        r in (-1, ROWS)
                        or c in (-1, COLS)
                        or heights[r][c] < heights[row][col]
                        or to_ocean[r][c]
                    ):
                        continue

                    queue.append((r, c))
                    to_ocean[r][c] = True
            
            return to_ocean

        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_pacific = [[False] * COLS for _ in range(ROWS)]
        to_atlantic = [[False] * COLS for _ in range(ROWS)]
        to_pacific_cells = deque()
        to_atlantic_cells = deque()
        res = []

        for row in range(ROWS):
            to_pacific_cells.append((row, 0))
            to_pacific[row][0] = True
            to_atlantic_cells.append((row, COLS - 1))
            to_atlantic[row][COLS - 1] = True

        for col in range(1, COLS):
            to_pacific_cells.append((0, col))
            to_pacific[0][col] = True
        
        for col in range(COLS - 1):
            to_atlantic_cells.append((ROWS - 1, col))
            to_atlantic[ROWS - 1][col] = True

        to_pacific = bfs(to_pacific_cells, to_pacific)
        to_atlantic = bfs(to_atlantic_cells, to_atlantic)

        for row in range(ROWS):
            for col in range(COLS):
                if to_pacific[row][col] and to_atlantic[row][col]:
                    res.append([row, col])

        return res


print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
print(Solution().pacificAtlantic([[1]]) == [[0, 0]])
print(Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
