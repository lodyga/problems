class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        ROWS = len(text1)
        COLS = len(text2)

        def dfs(index1, index2):
            if index1 == ROWS or index2 == COLS:
                return 0

            take = 0
            if text1[index1] == text2[index2]:
                take = dfs(index1 + 1, index2 + 1) + 1
            skip1 = dfs(index1 + 1, index2)
            skip2 = dfs(index1, index2 + 1)

            return max(take, skip1, skip2)

        return dfs(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array(memoization):
            A: top-down
        """
        ROWS = len(text1)
        COLS = len(text2)
        memo = [[-1] * COLS for _ in range(ROWS)]

        def dfs(index1, index2):
            if index1 == ROWS or index2 == COLS:
                return 0
            if memo[index1][index2] != -1:
                return memo[index1][index2]

            take = 0
            if text1[index1] == text2[index2]:
                take = 1 + dfs(index1 + 1, index2 + 1)
            skip1 = dfs(index1 + 1, index2)
            skip2 = dfs(index1, index2 + 1)

            memo[index1][index2] = max(take, skip1, skip2)
            return memo[index1][index2]

        return dfs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array(tabulation):
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
                        cache[row][col + 1]
                    )

        return cache[0][0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array(tabulation):
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
                        cache[col + 1]
                    )
            next_cache = cache

        return cache[0]


print(Solution().longestCommonSubsequence("abcde", "ace") == 3)
print(Solution().longestCommonSubsequence("abc", "abc") == 3)
print(Solution().longestCommonSubsequence("abc", "def") == 0)
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1)
print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4)
