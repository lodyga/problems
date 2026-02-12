class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
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

        def dfs(row: int, col: int) -> bool:
            if (
                row == -1 or row == ROWS or
                col == -1 or col == COLS
            ):
                return False
            elif visited[row][col]:
                return True
            elif grid[row][col]:
                visited[row][col] = True
                return True

            visited[row][col] = True
            is_closed = True

            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                is_closed &= dfs(r, c)
                
            return is_closed
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] == 0 and 
                    not visited[row][col]
                ):
                    res += dfs(row, col)
        
        return res


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
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
        visited = [[False] * COLS for _ in range(ROWS)]

        def bfs(row: int, col: int) -> bool:
            queue = deque([(row, col)])
            visited[row][col] = True
            is_closed = True
            
            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc

                    if (
                        r == -1 or r == ROWS or
                        c == -1 or c == COLS
                    ):
                        is_closed = False
                        continue
                    elif (visited[r][c] or grid[r][c]):
                        continue

                    queue.append((r, c))
                    visited[r][c] = True

            return is_closed

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    grid[row][col] == 0 and 
                    not visited[row][col]
                ):
                    res += bfs(row, col)
        
        return res


print(Solution().closedIsland([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 1)
print(Solution().closedIsland([[0, 1], [1, 1]]) == 0)
print(Solution().closedIsland([[1, 1, 1], [0, 0, 1], [1, 1, 1]]) == 0)
print(Solution().closedIsland([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 1)
print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) == 2)
print(Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1)
print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 2)
print(Solution().closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 5)
