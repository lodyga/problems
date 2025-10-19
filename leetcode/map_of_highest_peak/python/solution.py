from collections import deque


class Solution:
    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(is_water)
        COLS = len(is_water[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        
        def bfs():
            height = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                        if (
                            r == -1 or r == ROWS or
                            c == -1 or c == COLS or
                            is_water[r][c] != -1
                        ):
                            continue

                        queue.append((r, c))
                        is_water[r][c] = height + 1
                height += 1

        for row in range(ROWS):
            for col in range(COLS):
                if is_water[row][col]:
                    queue.append((row, col))
                    is_water[row][col] = 0
                else:
                    is_water[row][col] = -1
        
        bfs()        
        return is_water


class Solution:
    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(is_water)
        COLS = len(is_water[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        
        def bfs():
            height = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                        if (
                            r == -1 or r == ROWS or
                            c == -1 or c == COLS or
                            visited[r][c]
                        ):
                            continue

                        queue.append((r, c))
                        visited[r][c] = True
                        is_water[r][c] = height + 1
                height += 1

        for row in range(ROWS):
            for col in range(COLS):
                if is_water[row][col]:
                    queue.append((row, col))
                    visited[row][col] = True
                    is_water[row][col] = 0
        
        bfs()        
        return is_water


class Solution:
    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(is_water)
        COLS = len(is_water[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        
        def bfs():
            height = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    if visited[row][col]:
                        continue
                    
                    visited[row][col] = True
                    is_water[row][col] = height

                    for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                        if (
                            -1 < r < ROWS and
                            -1 < c < COLS and
                            not visited[r][c]
                        ):
                            queue.append((r, c))
                height += 1

        for row in range(ROWS):
            for col in range(COLS):
                if is_water[row][col]:
                    queue.append((row, col))
        
        bfs()        
        return is_water


print(Solution().highestPeak([[0, 1], [0, 0]]) == [[1, 0], [2, 1]])
print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]])