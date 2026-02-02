class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index: index + len(needle)] == needle:
                return index
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        def compare(start):
            for index in range(len(needle)):
                if needle[index] != haystack[index + start]:
                    return False
            return True

        for index in range(len(haystack) - len(needle) + 1):
            if compare(index):
                return index

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: Rabin-Karp, rolling hash
        """
        if len(needle) > len(haystack):
            return -1
        elif len(needle) == len(haystack):
            return 0 if needle == haystack else -1

        BASE = 29
        MOD = 10e9 + 7
        needle_hash = 0

        for letter in needle:
            val = ord(letter) - ord("a")
            needle_hash = (needle_hash * BASE + val) % MOD

        POWER = pow(BASE, len(needle) - 1, MOD)
        substr_hash = 0
        left = 0

        for right, letter in enumerate(haystack):
            val = ord(letter) - ord("a")
            substr_hash = (substr_hash * BASE + val) % MOD

            if right < len(needle) - 1:
                continue
            elif substr_hash == needle_hash:
                return left

            left_letter = haystack[left]
            left_val = ord(left_letter) - ord("a")
            substr_hash = (substr_hash - left_val * POWER) % MOD
            left += 1

        return -1


print(Solution().strStr("ab", "a") == 0)
print(Solution().strStr("ab", "b") == 1)
print(Solution().strStr("abc", "c") == 2)
print(Solution().strStr("aaa", "aaaa") == -1)
print(Solution().strStr("sadbutsad", "sad") == 0)
print(Solution().strStr("leetcode", "leeto") == -1)
print(Solution().strStr("hello", "ll") == 2)
print(Solution().strStr("ababcaababcaabc", "ababcaabc") == 6)
print(Solution().strStr("baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa", "bbaaaababa") == 107)
print(Solution().strStr("fourscoreandsevenyearsagoourfathersbroughtforthuponthiscontinentanewnation", "ourfathersbroughtforthuponthiscontinentanewnation") == 25)
