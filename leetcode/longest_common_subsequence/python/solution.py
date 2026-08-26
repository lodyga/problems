class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: brute-force
        """
        ROWS = len(text1)
        COLS = len(text2)

        def dfs(row: int, col: int) -> int:
            if row == ROWS or col == COLS:
                return 0

            elif text1[row] == text2[col]:
                res = 1 + dfs(row + 1, col + 1)

            else:
                res = max(
                    dfs(row + 1, col),
                    dfs(row, col + 1)
                )

            return res

        res = dfs(0, 0)
        return res


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array, string
            A: top-down
        """
        def dfs(row: int, col: int) -> int:
            if row == ROWS or col == COLS:
                return 0
            elif memo[row][col] != -1:
                return memo[row][col]

            elif text1[row] == text2[col]:
                memo[row][col] = 1 + dfs(row + 1, col + 1)
                return memo[row][col]

            memo[row][col] = max(
                dfs(row + 1, col),
                dfs(row, col + 1)
            )

            return memo[row][col]

        ROWS = len(text1)
        COLS = len(text2)
        memo = [[-1] * COLS for _ in range(ROWS)]
        return dfs(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array, string
            A: bottom-up
        """
        ROWS = len(text1)
        COLS = len(text2)
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if text1[row] == text2[col]:
                    cache[row][col] = 1 + cache[row + 1][col + 1]
                else:
                    cache[row][col] = max(
                        cache[row + 1][col],
                        cache[row][col + 1],
                    )

        return cache[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, string
            A: bottom-up
        """
        ROWS = len(text1)
        COLS = len(text2)
        next_cache = [0] * (COLS + 1)

        for row in range(ROWS - 1, -1, -1):
            cache = [0] * (COLS + 1)

            for col in range(COLS - 1, -1, -1):
                if text1[row] == text2[col]:
                    cache[col] = 1 + next_cache[col + 1]
                else:
                    cache[col] = max(
                        next_cache[col],
                        cache[col + 1],
                    )

            next_cache = cache

        return next_cache[0]


print(Solution().longestCommonSubsequence("abcde", "ace") == 3)
print(Solution().longestCommonSubsequence("abc", "abc") == 3)
print(Solution().longestCommonSubsequence("abc", "def") == 0)
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1)
print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4)
