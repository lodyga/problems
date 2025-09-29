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

            letter1 = text1[index1]
            letter2 = text2[index2]
            
            # skip letter
            sub_counter = dfs(index1 + 1, index2)
            
            if letter1 == letter2:
                # take letter
                sub_counter += dfs(index1 + 1, index2 + 1)

            return sub_counter

        return dfs(0, 0)


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index1, index2): distinct subesquences counter}

        def dfs(index1, index2):
            if index2 == len(text2):
                return 1
            elif index1 == len(text1):
                return 0
            elif (index1, index2) in memo:
                return memo[(index1, index2)]

            letter1 = text1[index1]
            letter2 = text2[index2]
            
            # skip letter
            sub_counter = dfs(index1 + 1, index2)
            
            if letter1 == letter2:
                # take letter
                sub_counter += dfs(index1 + 1, index2 + 1)

            memo[(index1, index2)] = sub_counter
            return sub_counter

        return dfs(0, 0)


class Solution:
    def numDistinct(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as array
        """
        # {(index1, index2): distinct subesquences counter}
        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(index1, index2):
            if index2 == len(text2):
                return 1
            elif index1 == len(text1):
                return 0
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            letter1 = text1[index1]
            letter2 = text2[index2]
            
            # skip letter
            sub_counter = dfs(index1 + 1, index2)
            
            if letter1 == letter2:
                # take letter
                sub_counter += dfs(index1 + 1, index2 + 1)

            memo[index1][index2] = sub_counter
            return sub_counter

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
                cache[row][col] = cache[row + 1][col]
                if text1[row] == text2[col]:
                    cache[row][col] += cache[row + 1][col + 1]
        
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
        next_cache = [0] * (COLS + 1)
        next_cache [-1] = 1

        for row in reversed(range(ROWS)):
            current_cache = [0] * (COLS + 1)
            current_cache[-1] = 1
            
            for col in reversed(range(COLS)):
                current_cache[col] = next_cache[col]
                if text1[row] == text2[col]:
                    current_cache[col] += next_cache[col + 1]
            
            next_cache = current_cache
    
        return next_cache[0]


print(Solution().numDistinct("rabbbit", "rabbit") == 3)
print(Solution().numDistinct("babgbag", "bag") == 5)
print(Solution().numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa") == 8556153)