r"""
draft
  b   a   g
b 5   3   2   1
a 2   3   2   1
b 2   1   2   1
g 1   1   2   1
b 1   1   1   1
a 0   1   1   1
g 0   0   1   1
  0   0   0   1

[i, j] = [i + 1, j] (+ if i==j [i + 1, j + 1])
"""

class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index1, index2):
            if index2 == len(text2):
                return 1
            elif index1 == len(text1):
                return 0
            
            memo = dfs(index1 + 1, index2)
            
            if text1[index1] == text2[index2]:
                memo += dfs(index1 + 1, index2 + 1)
            
            return memo
        
        return dfs(0, 0)


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index1, index2): is_matched}

        def dfs(index1, index2):
            if index2 == len(text2):
                return 1
            elif index1 == len(text1):
                return 0
            elif (index1, index2) in memo:
                return memo[(index1, index2)]
            
            memo[(index1, index2)] = dfs(index1 + 1, index2)
            
            if text1[index1] == text2[index2]:
                memo[(index1, index2)] += dfs(index1 + 1, index2 + 1)
            
            return memo[(index1, index2)]
        
        return dfs(0, 0)


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as array
        """
        memo = [[None] * len(text2) for _ in range((len(text1)))]
    
        def dfs(index1, index2):
            if index2 == len(text2):
                return 1
            elif index1 == len(text1):
                return 0
            elif memo[index1][index2] is not None:
                return memo[index1][index2]
            elif text1[index1] == text2[index2]:
                memo[index1][index2] = dfs(index1 + 1, index2) + dfs(index1 + 1, index2 + 1)
            else:
                memo[index1][index2] = dfs(index1 + 1, index2)

            return memo[index1][index2]
        
        return dfs(0, 0)


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up
        """
        ROWS = len(text1)
        COLS = len(text2)
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for row in range(ROWS + 1):
            cache[row][COLS] = 1

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if text1[row] == text2[col]:
                    cache[row][col] = cache[row + 1][col] + cache[row + 1][col + 1]
                else:
                    cache[row][col] = cache[row + 1][col]
    
        return cache[0][0]


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        ROWS = len(text1)
        COLS = len(text2)
        next_row = [0] * (COLS + 1)
        next_row [-1] = 1

        for row in reversed(range(ROWS)):
            current_row = [0] * (COLS + 1)
            current_row[-1] = 1
            
            for col in reversed(range(COLS)):
                if text1[row] == text2[col]:
                    current_row[col] = next_row[col] + next_row[col + 1]
                else:
                    current_row[col] = next_row[col]
            
            next_row = current_row.copy()
    
        return next_row[0]


print(Solution().numDistinct("rabbbit", "rabbit") == 3)
print(Solution().numDistinct("babgbag", "bag") == 5)
print(Solution().numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa") == 8556153)

