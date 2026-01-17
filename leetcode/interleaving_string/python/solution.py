class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), string
            A: top-down
        """
        if len(s1) + len(s2) != len(s3):
            return False

        # {(index1, index2): can_fold}
        # can_fold: {1: Yes, 0: No, -1: donno}
        memo = [[-1] * len(s2) for _ in range(len(s1))]

        def dfs(index1: int, index2: int) -> int:
            index3 = index1 + index2

            if index1 == len(s1):
                return s3[index3:] == s2[index2:]
            elif index2 == len(s2):
                return s3[index3:] == s1[index1:]
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            letter1 = s1[index1]
            letter2 = s2[index2]
            letter3 = s3[index3]

            if letter1 == letter3 and dfs(index1 + 1, index2):
                memo[index1][index2] = 1
                return 1
            elif letter2 == letter3 and dfs(index1, index2 + 1):
                memo[index1][index2] = 1
                return 1
            
            memo[index1][index2] = 0
            return 0

        return dfs(0, 0) == 1


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix), string
            A: bottom-up
        """
        if len(s3) != len(s1) + len(s2):
            return False
        
        ROWS = len(s1)
        COLS = len(s2)
        cache = [[False] * (COLS + 1) for _ in range(ROWS + 1)]
        cache[ROWS][COLS] = True

        for row in range(ROWS, -1, -1):
            for col in range(COLS, -1, -1):
                index = row + col
                
                if (
                    row < ROWS and 
                    s1[row] == s3[index] and 
                    cache[row + 1][col]
                ):
                    cache[row][col] = True
                elif (
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
        Tags:
            DS: array (matrix), string
            A: bottom-up
        """
        if len(s3) != len(s1) + len(s2):
            return False
        
        ROWS = len(s1)
        COLS = len(s2)
        next_cache = [False] * (COLS + 1)
        next_cache[COLS] = True

        for row in range(ROWS, -1, -1):
            cache = [False] * (COLS + 1)
            if row == ROWS:
                cache[COLS] = True

            for col in range(COLS, -1, -1):
                index = row + col
                
                if (
                    row < ROWS and 
                    s1[row] == s3[index] and 
                    next_cache[col]
                ):
                    cache[col] = True
                elif (
                    col < COLS and 
                    s2[col] == s3[index] and 
                    cache[col + 1]
                ):
                    cache[col] = True
            
            next_cache = cache
        
        return next_cache[0]


print(Solution().isInterleave("a", "b", "c") == False)
print(Solution().isInterleave("aa", "bb", "aabb") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)
print(Solution().isInterleave("", "", "") == True)
print(Solution().isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb", "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb") == True)
