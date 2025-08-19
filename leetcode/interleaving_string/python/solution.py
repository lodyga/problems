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

            first = second = False
            index = index1 + index2

            if (
                index1 < len(s1) and
                s1[index1] == s3[index]
            ):
                first = dfs(index1 + 1, index2)
            if (
                index2 < len(s2) and
                s2[index2] == s3[index]
            ):
                second = dfs(index1, index2 + 1)

            return first or second

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down witm memoization as hash map
        """
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}  # {(index1, index2):  can fold}

        def dfs(index1, index2):
            if index1 + index2 == len(s3):
                return True
            elif (index1, index2) in memo:
                return memo[(index1, index2)]

            first = second = False
            index = index1 + index2

            if (
                index1 < len(s1) and
                s1[index1] == s3[index]
            ):
                first = dfs(index1 + 1, index2)
            if (
                not first and
                index2 < len(s2) and
                s2[index2] == s3[index]
            ):
                second = dfs(index1, index2 + 1)

            memo[(index1, index2)] = first or second
            return memo[(index1, index2)]

        return dfs(0, 0)


print(Solution().isInterleave("aa", "bb", "aabb") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)
print(Solution().isInterleave("", "", "") == True)
print(Solution().isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb", "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb") == True)