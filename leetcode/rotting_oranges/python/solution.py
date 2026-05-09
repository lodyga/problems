class Solution:
    def orangesRotting(self, grid: list[list[float]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), queue
            A: multi-source BFS
        """
        from collections import deque
        UPPER_BOUND = 101
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [row.copy() for row in grid]
        queue = deque()

        def bfs() -> None:
            distance = -1

            while queue:
                distance += 1

                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (row + dr, col + dc)

                        if (
                            r in (-1, ROWS) or
                            c in (-1, COLS) or
                            visited[r][c] != -1
                        ):
                            continue

                        queue.append((r, c))
                        visited[r][c] = distance + 1

            return distance

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited[row][col] = 0
                elif grid[row][col] == 1:
                    visited[row][col] = -1

        max_distance = bfs()
        is_unreachable = any(
            True for row in visited for cell in row if cell == -1)

        if is_unreachable:
            return -1
        elif max_distance == -1:
            return 0
        else:
            return max_distance


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
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
        max_distance = 0

        def bfs() -> int:
            max_distance = 0
            
            while queue:
                (row, col, distance) = queue.popleft()
                max_distance = max(max_distance, distance)

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)
                    if (
                        -1 < r < ROWS and
                        -1 < c < COLS and
                        grid[r][c] == -1
                    ):
                        queue.append((r, c, distance + 1))
                        grid[r][c] = distance + 1
            return max_distance
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    grid[row][col] = 0
                elif grid[row][col] == 1:
                    grid[row][col] = -1

        max_distance = bfs()
        is_unreachable = any(True for row in grid for cell in row if cell == -1)
        return -1 if is_unreachable else max_distance


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
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
        max_distance = 0

        def bfs() -> int:
            max_distance = -1
            
            while queue:
                for index in range(len(queue)):
                    (row, col) = queue.popleft()
                    if index == 0:
                        max_distance += 1
                    
                    for dr, dc in DIRECTIONS:
                        (r, c) = (row + dr, col + dc)
                        if (
                            -1 < r < ROWS and
                            -1 < c < COLS and
                            grid[r][c] == 1
                        ):
                            queue.append((r, c))
                            grid[r][c] = 0
            
            return max(max_distance, 0)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    grid[row][col] = 0

        max_distance = bfs()
        is_unreachable = any(True for row in grid for cell in row if cell == 1)
        return -1 if is_unreachable else max_distance


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4)
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1)
print(Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2)
print(Solution().orangesRotting([[0, 2]]) == 0)
print(Solution().orangesRotting([[0]]) == 0)
print(Solution().orangesRotting([[1]]) == -1)
print(Solution().orangesRotting([[0, 0, 2, 1, 0, 1], [1, 2, 1, 1, 2, 1], [2, 1, 2, 2, 2, 0], [2, 2, 1, 0, 0, 2], [2, 2, 1, 0, 2, 2], [2, 1, 1, 2, 2, 0], [2, 2, 1, 0, 1, 1], [2, 1, 2, 1, 0, 1], [2, 1, 2, 2, 2, 2]]) == 2)
