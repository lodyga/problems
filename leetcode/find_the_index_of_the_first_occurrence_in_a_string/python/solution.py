class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp
        """
        if len(needle) > len(haystack):
            return -1
        
        def letter_value(letter):
            return ord(letter) - ord("a")

        BASE = 29
        MOD = 10**9 + 7
        needle_hash = 0
        haystack_hash = 0
        power = 1

        for index in range(len(needle)):
            needle_letter = needle[index]
            haystack_letter = haystack[index]
            needle_hash = (needle_hash * BASE + letter_value(needle_letter)) % MOD
            haystack_hash = (haystack_hash * BASE + letter_value(haystack_letter)) % MOD
        
        power = pow(BASE, len(needle) - 1, MOD)

        for left in range(len(haystack) - len(needle) + 1):
            if needle_hash == haystack_hash:
                return left
            elif left < len(haystack) - len(needle):
                right = left + len(needle)
                haystack_hash = (haystack_hash - letter_value(haystack[left]) * power) % MOD
                haystack_hash = (haystack_hash * BASE + letter_value(haystack[right])) % MOD
        
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: iteration
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
        Tags: iteration
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


print(Solution().strStr("ab", "a") == 0)
print(Solution().strStr("ab", "b") == 1)
print(Solution().strStr("abc", "c") == 2)
print(Solution().strStr("aaa", "aaaa") == -1)
print(Solution().strStr("sadbutsad", "sad") == 0)
print(Solution().strStr("leetcode", "leeto") == -1)
print(Solution().strStr("hello", "ll") == 2)
print(Solution().strStr("ababcaababcaabc", "ababcaabc") == 6)
print(Solution().strStr("baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa", "bbaaaababa") == 107)