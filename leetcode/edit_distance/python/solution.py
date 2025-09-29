r"""
draft
    a   d   c
a   1   2   2   3
b   2   1   1   2
c   2   1   0   1
    3   2   1   0
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(3^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index1, index2):
            if index1 == len(word1):
                return len(word2) - index2
            elif index2 == len(word2):
                return len(word1) - index1

            if word1[index1] == word2[index2]:
                # match
                distance = dfs(index1 + 1, index2 + 1)
            else:
                # insert
                insert_char = dfs(index1, index2 + 1)
                # delete
                delete_char = dfs(index1 + 1, index2)
                # replace
                replace_char = dfs(index1 + 1, index2 + 1)
                distance = min(insert_char, delete_char, replace_char) + 1

            return distance

        return dfs(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index1, index2): min distance}

        def dfs(index1, index2):
            if index1 == len(word1):
                return len(word2) - index2
            elif index2 == len(word2):
                return len(word1) - index1
            elif (index1, index2) in memo:
                return memo[(index1, index2)]

            if word1[index1] == word2[index2]:
                # match
                distance = dfs(index1 + 1, index2 + 1)
            else:
                # insert
                insert_char = dfs(index1, index2 + 1)
                # delete
                delete_char = dfs(index1 + 1, index2)
                # replace
                replace_char = dfs(index1 + 1, index2 + 1)
                distance = min(insert_char, delete_char, replace_char) + 1

            memo[(index1, index2)] = distance
            return distance

        return dfs(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up with tabulation as array
        """
        ROWS = len(word1)
        COLS = len(word2)
        # [[index1][index2]: min distance]
        cache = [[ROWS + COLS] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for row in range(ROWS + 1):
            cache[row][COLS] = ROWS - row
        for col in range(COLS + 1):
            cache[ROWS][col] = COLS - col

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if word1[row] == word2[col]:
                    # match
                    cache[row][col] = cache[row + 1][col + 1]
                else:
                    cache[row][col] = 1 + min(
                        # replace
                        cache[row + 1][col + 1],
                        # delete
                        cache[row + 1][col],
                        # insert
                        cache[row][col + 1]
                    )
        
        return cache[0][0]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as array
        """
        ROWS = len(word1)
        COLS = len(word2)
        # [index: min distance]
        next_cache = [COLS - col for col in range(COLS + 1)]
        
        for row in reversed(range(ROWS)):
            cache = [ROWS - row] * (COLS + 1)
            
            for col in reversed(range(COLS)):
                if word1[row] == word2[col]:
                    # match
                    cache[col] = next_cache[col + 1]
                else:
                    cache[col] = 1 + min(
                        # replace
                        next_cache[col + 1],
                        # delete
                        next_cache[col],
                        # insert
                        cache[col + 1]
                    )
            next_cache = cache
        
        return next_cache[0]


print(Solution().minDistance("a", "a") == 0)
print(Solution().minDistance("", "b") == 1)
print(Solution().minDistance("b", "") == 1)
print(Solution().minDistance("a", "b") == 1)
print(Solution().minDistance("ab", "b") == 1)
print(Solution().minDistance("ba", "b") == 1)
print(Solution().minDistance("b", "ba") == 1)
print(Solution().minDistance("aa", "b") == 2)
print(Solution().minDistance("horse", "ros") == 3)
print(Solution().minDistance("intention", "execution") == 5)
print(Solution().minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine") == 6)