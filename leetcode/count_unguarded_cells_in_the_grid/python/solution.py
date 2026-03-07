class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        from collections import deque
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: queue, array (matrix)
            A: multi-source BFS
        """
        ROWS = m
        COLS = n
        DIRECTIONS = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
        # 1: not visited/safe; 0: visited/not safe; -1: wall/guard
        grid = [[1] * COLS for _ in range(ROWS)]
        queue = deque()

        for row, col in walls:
            grid[row][col] = -1

        for row, col in guards:
            grid[row][col] = -1

            for direction in range(4):
                queue.append((row, col, direction))

        # bfs
        while queue:
            row, col, direction = queue.popleft()
            dr, dc = DIRECTIONS[direction]
            (r, c) = (row + dr, col + dc)

            if (
                r == -1 or r == ROWS or
                c == -1 or c == COLS or
                grid[r][c] == -1
            ):
                continue

            queue.append((r, c, direction))
            grid[r][c] = 0

        return sum(sum(row) for row in grid) + len(guards) + len(walls)


print(Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]) == 7)
print(Solution().countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4)
print(Solution().countUnguarded(2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]) == 1)
