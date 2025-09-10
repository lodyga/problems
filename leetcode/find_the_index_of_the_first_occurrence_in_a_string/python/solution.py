class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index: index + len(needle)] == needle:
                return index
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        for index in range(len(haystack) - len(needle) + 1):
            index2 = 0
            while index2 < len(needle):
                if haystack[index + index2] != needle[index2]:
                    break
                index2 += 1
            if index2 == len(needle):
                return index
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp
        """
        if len(needle) > len(haystack):
            return -1
        
        base = 29
        needle_hash = 0
        haystack_hash = 0
        mod = 10**9 + 7
        power = 1

        for index in range(len(needle)):
            needle_hash = (needle_hash * base + (ord(needle[index]) - ord("a"))) % mod
            haystack_hash = (haystack_hash * base + (ord(haystack[index]) - ord("a"))) % mod
        
        power = pow(base, len(needle) - 1, mod)

        for left in range(len(haystack) - len(needle) + 1):
            right = left + len(needle)

            if needle_hash == haystack_hash:
                return left
            elif left < len(haystack) - len(needle):
                haystack_hash = (haystack_hash - (ord(haystack[left]) - ord("a")) * power) % mod
                haystack_hash = (haystack_hash * base + (ord(haystack[right]) - ord("a"))) % mod
        
        return -1


print(Solution().strStr("ab", "a"), 0)
print(Solution().strStr("ab", "b"), 1)
print(Solution().strStr("abc", "c"), 2)
print(Solution().strStr("aaa", "aaaa"), -1)
print(Solution().strStr("sadbutsad", "sad"), 0)
print(Solution().strStr("leetcode", "leeto"), -1)