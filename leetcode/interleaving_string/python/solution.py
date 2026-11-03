class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), string
            A: top-down
        """
        def dfs(idx1: int, idx2: int) -> bool:
            idx3 = idx1 + idx2
            res = False

            if idx1 == ROWS:
                return s2[idx2:] == s3[idx3:]

            elif idx2 == COLS:
                return s1[idx1:] == s3[idx3:]

            elif memo[idx1][idx2] != -1:
                return bool(memo[idx1][idx2])

            if s1[idx1] == s3[idx3]:
                res = dfs(idx1 + 1, idx2)

            if s2[idx2] == s3[idx3]:
                res = res or dfs(idx1, idx2 + 1)

            memo[idx1][idx2] = int(res)
            return res

        ROWS = len(s1)
        COLS = len(s2)

        if ROWS + COLS != len(s3):
            return False

        memo = [[-1] * COLS for _ in range(ROWS)]

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), string
            A: bottom-up
        """
        ROWS = len(s1)
        COLS = len(s2)

        if ROWS + COLS != len(s3):
            return False

        cache = [[False] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[ROWS][COLS] = True

        for row in range(ROWS, -1, -1):
            for col in range(COLS, -1, -1):
                idx = row + col

                if (
                    row < ROWS
                    and s1[row] == s3[idx]
                    and cache[row + 1][col]
                ):
                    cache[row][col] = True
                elif (
                    col < COLS
                    and s2[col] == s3[idx]
                    and cache[row][col + 1]
                ):
                    cache[row][col] = True

        return cache[0][0]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (matrix), string
            A: bottom-up
        """
        ROWS = len(s1)
        COLS = len(s2)

        if ROWS + COLS != len(s3):
            return False

        next_cache = [False] * (COLS + 1)
        next_cache[COLS] = True

        for row in range(ROWS, -1, -1):
            cache = [False] * (COLS + 1)

            if row == ROWS:
                cache[COLS] = True

            for col in range(COLS, -1, -1):
                idx = row + col

                if (
                    row < ROWS
                    and s1[row] == s3[idx]
                    and next_cache[col]
                ):
                    cache[col] = True
                elif (
                    col < COLS
                    and s2[col] == s3[idx]
                    and cache[col + 1]
                ):
                    cache[col] = True

            next_cache = cache

        return next_cache[0]


print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)
print(Solution().isInterleave("", "", "") == True)
print(Solution().isInterleave("a", "b", "c") == False)
print(Solution().isInterleave("aa", "bb", "aabb") == True)
print(Solution().isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb", "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb") == True)
print(Solution().isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab") == False)
