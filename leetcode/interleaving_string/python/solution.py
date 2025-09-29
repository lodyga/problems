class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(2^n)
            n: s3.length
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(index1, index2):
            if index1 + index2 == len(s3):
                return True

            index = index1 + index2
            memo = False

            if (
                index1 < len(s1) and
                s1[index1] == s3[index]
            ):
                memo |= dfs(index1 + 1, index2)
            if (
                not memo and
                index2 < len(s2) and
                s2[index2] == s3[index]
            ):
                memo |= dfs(index1, index2 + 1)

            return memo

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down witm memoization as hash map
        """
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        if s3_len != s1_len + s2_len:
            return False
        
        memo = {}  # {(index1, index2):  can fold}

        def dfs(index1, index2):
            if (index1 + index2 == s3_len):
                return True
            elif (index1, index2) in memo:
                return memo[(index1, index2)]
            
            index3 = index1 + index2          
            memo[(index1, index2)] = False
            
            if (
                index1 < s1_len and 
                s3[index3] == s1[index1]
            ):
                memo[(index1, index2)] |= dfs(index1 + 1, index2)
            if (
                not memo[(index1, index2)] and
                index2 < s2_len and 
                s3[index3] == s2[index2]
            ):
                memo[(index1, index2)] |= dfs(index1, index2 + 1)
            
            return memo[(index1, index2)]

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up with cache as array
        """
        ROWS = len(s1)
        COLS = len(s2)
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        cache = [[False] * (COLS + 1) for _ in range(ROWS + 1)]  # [[index1, index2]: can fold]
        cache[ROWS][COLS] = True

        for row in reversed(range(ROWS + 1)):
            for col in reversed(range(COLS + 1)):
                index = row + col
                if (
                    row < ROWS and 
                    s1[row] == s3[index] and 
                    cache[row + 1][col]
                ):
                    cache[row][col] = True
                    continue
                if (
                    col < COLS and 
                    s2[col] == s3[index] and 
                    cache[row][col + 1]
                ):
                    cache[row][col] = True
        
        return cache[0][0]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with cache as array
        """
        ROWS = len(s1)
        COLS = len(s2)
        
        if len(s3) != len(s1) + len(s2):
            return False
        

        for row in reversed(range(ROWS + 1)):
            cache = [False] * (COLS + 1)  # [[index1, index2]: can fold]
            if row == ROWS:
                cache[COLS] = True

            for col in reversed(range(COLS + 1)):
                index = row + col
                if (
                    row < ROWS and 
                    s1[row] == s3[index] and 
                    next_cache[col]
                ):
                    cache[col] = True
                    continue
                if (
                    col < COLS and 
                    s2[col] == s3[index] and 
                    cache[col + 1]
                ):
                    cache[col] = True
            
            next_cache = cache
        
        return cache[0]


print(Solution().isInterleave("a", "b", "c") == False)
print(Solution().isInterleave("aa", "bb", "aabb") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)
print(Solution().isInterleave("", "", "") == True)
print(Solution().isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb", "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb") == True)