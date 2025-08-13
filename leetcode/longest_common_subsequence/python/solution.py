r"""
draft
    a   z   b
a   2   1   1
b   1   1   1
c   0   0   0
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up
        """
        rows = len(text1)
        cols = len(text2)
        cache = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    cache[row][col] = cache[row + 1][col + 1] + 1
                else:
                    cache[row][col] = max(
                        cache[row + 1][col], 
                        cache[row][col + 1])
            
        return cache[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        rows = len(text1)
        cols = len(text2)
        cache = [0] * (cols + 1)
        
        for row in reversed(range(rows)):
            prev_cache = [0] * (cols + 1)
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    prev_cache[col] = cache[col + 1] + 1
                else:
                    prev_cache[col] = max(
                        cache[col], 
                        prev_cache[col + 1])
            cache = prev_cache
            
        return cache[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as array
        """
        rows = len(text1)
        cols = len(text2)
        memo = [[None] * cols for _ in range(rows)]
        
        def dfs(row, col):
            if (
                row == rows or
                col == cols
            ):
                return 0
            elif memo[row][col] is not None:
                return memo[row][col]
            elif text1[row] == text2[col]:
                memo[row][col] = dfs(row + 1, col + 1) + 1
            else:
                memo[row][col] = max(
                    dfs(row + 1, col), 
                    dfs(row, col + 1)
                )
            return memo[row][col]
        
        return dfs(0, 0)


print(Solution().longestCommonSubsequence("abcde", "ace") == 3)
print(Solution().longestCommonSubsequence("abc", "abc") == 3)
print(Solution().longestCommonSubsequence("abc", "def") == 0)
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1)
print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4)