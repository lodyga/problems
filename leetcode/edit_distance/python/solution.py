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
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
        """
        UPPER_BOUND = len(word1) + len(word2)
        # memo = [(index1, index2): min distance]
        memo = [[-1] * len(word2) for _ in range(len(word1))]

        def dfs(index1: int, index2: int) -> int:
            if (
                index1 == len(word1) or
                index2 == len(word2)
            ):
                return len(word2) - index2 or len(word1) - index1
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            # if letter match
            if word1[index1] == word2[index2]:
                distance = dfs(index1 + 1, index2 + 1)
            else:
                insert_chr = 1 + dfs(index1, index2 + 1)
                delete_chr = 1 + dfs(index1 + 1, index2)
                replace_chr = 1 + dfs(index1 + 1, index2 + 1)
                distance = min(insert_chr, delete_chr, replace_chr)

            memo[index1][index2] = distance
            return distance

        return dfs(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        # cache = [(index1, index2): min distance]
        ROWS = len(word1)
        COLS = len(word2)
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for row in range(ROWS):
            cache[row][COLS] = ROWS - row
        
        for col in range(COLS):
            cache[ROWS][col] = COLS - col

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                # if letter match
                if word1[row] == word2[col]:
                    cache[row][col] = cache[row + 1][col + 1]
                else:
                    cache[row][col] = 1 + min(
                        # insert
                        cache[row][col + 1],
                        # delete
                        cache[row + 1][col],
                        # replace
                        cache[row + 1][col + 1]
                    )

        return cache[0][0]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        # cache = [index2: min distance]
        ROWS = len(word1)
        COLS = len(word2)
        next_cache = list(range(COLS, -1, -1))

        for row in range(ROWS - 1, -1, -1):
            cache = [ROWS - row] * (COLS + 1)
            
            for col in range(COLS - 1, -1, -1):
                # if letter match
                if word1[row] == word2[col]:
                    cache[col] = next_cache[col + 1]
                else:
                    cache[col] = 1 + min(
                        # insert
                        cache[col + 1],
                        # delete
                        next_cache[col],
                        # replace
                        next_cache[col + 1]
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
