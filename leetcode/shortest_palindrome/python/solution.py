class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers, tle
        """
        palindrome = ""

        def is_palindrome(l, r):
            while l < r:
                if text[l] == text[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        for index in reversed(range(len(text))):
            if is_palindrome(0, index):
                palindrome = text[index + 1:][::-1] + text
                break

        return palindrome


class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp
        """
        prefix = 0
        suffix = 0
        base = 29
        last_index = 0
        mod = 10**9 + 7

        for index, letter in enumerate(text):
            number = (ord(letter) - ord("a") + 1)
            prefix = ((prefix * base) + number) % mod
            suffix = ((number * base**index) + suffix) % mod

            if prefix == suffix:
                last_index = index

        return text[last_index + 1:][::-1] + text


print(Solution().shortestPalindrome("aacecaaa"), "aaacecaaa")
print(Solution().shortestPalindrome("abcd"), "dcbabcd")
print(Solution().shortestPalindrome("aacecaaa") == "aaacecaaa")
print(Solution().shortestPalindrome("abcd") == "dcbabcd")
print(Solution().shortestPalindrome("") == "")