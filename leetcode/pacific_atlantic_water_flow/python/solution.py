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
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_pacific = [[False] * COLS for _ in range(ROWS)]
        to_atlantic = [[False] * COLS for _ in range(ROWS)]

        def dfs(row, col, prev_height, to_ocean):
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                heights[row][col] < prev_height or
                to_ocean[row][col] is True
            ):
                return

            to_ocean[row][col] = True
            
            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                dfs(r, c, heights[row][col], to_ocean)

        for row in range(ROWS):
            dfs(row, 0, 0, to_pacific)
            dfs(row, COLS - 1, 0, to_atlantic)
        for col in range(COLS):
            dfs(0, col, 0, to_pacific)
            dfs(ROWS - 1, col, 0, to_atlantic)

        to_ocean_tiles = []
        for row in range(ROWS):
            for col in range(COLS):
                if to_pacific[row][col] and to_atlantic[row][col]:
                    to_ocean_tiles.append([row, col])

        return to_ocean_tiles


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
            n: heights length
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), hash set
            A: multi-source DFS
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_pacific = set()
        to_atlantic = set()

        def dfs(row, col, prev_height, ocean):
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                heights[row][col] < prev_height or
                (row, col) in ocean
            ):
                return

            ocean.add((row, col))
            
            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                dfs(r, c, heights[row][col], ocean)

        for row in range(ROWS):
            dfs(row, 0, 0, to_pacific)
            dfs(row, COLS - 1, 0, to_atlantic)

        for col in range(COLS):
            dfs(0, col, 0, to_pacific)
            dfs(ROWS - 1, col, 0, to_atlantic)
        
        return [[row, col] for row, col in to_pacific & to_atlantic]


from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
            n: heights length
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: multi-source BFS, iteration, queue
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_pacific = [[False] * COLS for _ in range(ROWS)]
        to_atlantic = [[False] * COLS for _ in range(ROWS)]

        def bfs(ocean_queue, to_ocean):
            while ocean_queue:
                row, col = ocean_queue.popleft()
                to_ocean[row][col] = True

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                    if (
                        r == -1 or
                        c == -1 or
                        r == ROWS or
                        c == COLS or
                        heights[r][c] < heights[row][col] or
                        to_ocean[r][c] is True
                    ): 
                        continue

                    ocean_queue.append((r, c))
                    to_ocean[r][c] = True

        pacific_queue = deque()
        atlantic_queue = deque()
        for row in range(ROWS):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, COLS - 1))
        for col in range(COLS):
            pacific_queue.append((0, col))
            atlantic_queue.append((ROWS - 1, col))

        bfs(pacific_queue, to_pacific)
        bfs(atlantic_queue, to_atlantic)

        to_ocean_tiles = []
        for row in range(ROWS):
            for col in range(COLS):
                if to_pacific[row][col] and to_atlantic[row][col]:
                    to_ocean_tiles.append([row, col])

        return to_ocean_tiles


print(sorted(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))
print(sorted(Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]])) == sorted([[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]))
print(sorted(Solution().pacificAtlantic([[1]])) == sorted([[0, 0]]))
