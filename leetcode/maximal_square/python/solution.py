class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = [[1 if matrix[row][col] == "1" else 0
                  for col in range(COLS)] for row in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if cache[row][col] and row > 0 and col > 0:
                    cache[row][col] = 1 + min(
                        cache[row - 1][col],
                        cache[row][col - 1],
                        cache[row - 1][col - 1]
                    )

        return max(max(cache[row]) for row in range(ROWS)) ** 2


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        prev_cache = [0] * COLS
        max_side = 0

        for row in range(ROWS):
            cache = [1 if matrix[row][col] == "1" else 0
                     for col in range(COLS)]

            for col in range(COLS):
                if cache[col] and row > 0 and col > 0:
                    cache[col] = 1 + min(
                        prev_cache[col],
                        cache[col - 1],
                        prev_cache[col - 1]
                    )

            prev_cache = cache
            max_side = max(max_side, max(cache))

        return max_side ** 2


print(Solution().maximalSquare([["1", "1"]]) == 1)
print(Solution().maximalSquare([["1", "1"], ["1", "1"]]) == 4)
print(Solution().maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4)
print(Solution().maximalSquare([["0", "1"], ["1", "0"]]) == 1)
print(Solution().maximalSquare([["0"]]) == 0)
print(Solution().maximalSquare([["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1"]]) == 16)


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        from collections import deque
        """
        Time complexity: O(n4)
        Auxiliary space complexity: O(n2)
        Tags: brute-force, bfs, iteration, queue, matrix
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        DIRECTIONS = ((0, 1), (1, 1), (1, 0))

        def bfs(row, col):
            queue = deque([(row, col)])
            visited = set([(row, col)])
            dist = 1
            max_square_side = 1
            is_break = False

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    
                    for r, c in ((r + row, c + col) for r, c in DIRECTIONS):
                        if (r, c) in visited:
                            continue
                        elif r == ROWS or c == COLS or matrix[r][c] == "0":
                            is_break = True
                            break
                        
                        queue.append((r, c))
                        visited.add((r, c))
                                        
                if not is_break:
                    dist += 1
                    max_square_side = max(max_square_side, dist)

            return max_square_side ** 2

        max_square = 0
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "1":
                    max_square = max(max_square, bfs(row, col))
        return max_square


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as array
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # [i, j]: max square side for i, j being top left corner
        memo = [[-1] * COLS for _ in range(ROWS)]

        def dfs(row, col):
            if row == ROWS or col == COLS:
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]
            elif matrix[row][col] == "0":
                memo[row][col] = 0
                return 0

            side = min(
                dfs(row, col + 1),
                dfs(row + 1, col),
                dfs(row + 1, col + 1)
            )
            
            memo[row][col] = side + 1
            return side + 1

        max_side = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_side = max(max_side, dfs(row, col))
        
        return max_side**2


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # [i, j]: max square side for i, j being top left corner
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        max_side = 0

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if matrix[row][col] == "1":
                    side = min(
                        cache[row][col + 1],
                        cache[row + 1][col],
                        cache[row + 1][col + 1]
                    )
                    cache[row][col] = 1 + side
                    max_side = max(max_side, 1 + side)
        
        return max_side**2


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # [i, j]: max square side for i, j being top left corner
        blank_cache = [0] * (COLS + 1)
        next_cache = blank_cache
        max_side = 0

        for row in reversed(range(ROWS)):
            cache = blank_cache.copy()
            for col in reversed(range(COLS)):
                if matrix[row][col] == "1":
                    side = min(
                        cache[col + 1],
                        next_cache[col],
                        next_cache[col + 1]
                    )
                    cache[col] = 1 + side
                    max_side = max(max_side, 1 + side)
            next_cache = cache
        
        return max_side**2