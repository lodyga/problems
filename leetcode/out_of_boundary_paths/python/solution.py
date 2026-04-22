class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n3)
        Tags:
            DS: array
            A: top-down
        """
        MOD = 10**9 + 7
        ROWS = m
        COLS = n
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        memo = [[[-1] * maxMove for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col, moves):
            if (
                row == -1 or row == ROWS or
                col == -1 or col == COLS
            ):
                return 1
            elif moves == maxMove:
                return 0
            elif memo[row][col][moves] != -1:
                return memo[row][col][moves]

            res = sum(
                dfs(dr + row, dc + col, moves + 1)
                for (dr, dc) in DIRECTIONS
            ) % MOD
            memo[row][col][moves] = res
            return res

        return dfs(startRow, startColumn, 0)


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n3)
        Tags:
            DS: array
            A: bottom-up
        """
        MOD = 10**9 + 7
        ROWS = m
        COLS = n
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        cache = [[[0] * (maxMove + 1) for _ in range(COLS)]
                 for _ in range(ROWS)]

        for move in range(maxMove - 1, -1, -1):
            for row in range(ROWS):
                for col in range(COLS):
                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (dr + row, dc + col)

                        if (
                            r == -1 or r == ROWS or
                            c == -1 or c == COLS
                        ):
                            cache[row][col][move] += 1
                        else:
                            cache[row][col][move] += cache[r][c][move + 1]
                    
                    cache[row][col][move] %= MOD

        return cache[startRow][startColumn][0]


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        MOD = 10**9 + 7
        ROWS = m
        COLS = n
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        next_cache = [[0] * COLS for _ in range(ROWS)]

        for _ in range(maxMove - 1, -1, -1):
            cache = [[0] * COLS for _ in range(ROWS)]
            
            for row in range(ROWS):
                for col in range(COLS):
                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (dr + row, dc + col)

                        if (
                            r == -1 or r == ROWS or
                            c == -1 or c == COLS
                        ):
                            cache[row][col] += 1
                        else:
                            cache[row][col] += next_cache[r][c]
            
            next_cache = cache

        return next_cache[startRow][startColumn]


print(Solution().findPaths(2, 2, 0, 0, 0) == 0)
print(Solution().findPaths(2, 2, 1, 0, 0) == 2)
print(Solution().findPaths(2, 2, 2, 0, 0) == 6)
print(Solution().findPaths(1, 3, 3, 0, 1) == 12)
print(Solution().findPaths(8, 7, 16, 1, 5) == 102984580)
