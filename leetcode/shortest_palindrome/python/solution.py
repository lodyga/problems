class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: Rabin-Karp, rolling hash
        """
        BASE = 29
        MOD = 10**9 + 7
        prefix = 0
        suffix = 0
        power = 1
        last_index = 0

        for index, letter in enumerate(text):
            value = ord(letter) - ord("a")
            prefix = (prefix*BASE + value) % MOD
            suffix = (value*power + suffix) % MOD
            power = (power * BASE) % MOD

            if prefix == suffix:
                last_index = index

        return text[last_index + 1:][::-1] + text


class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers
        """
        def isPalindrome(left, right):
            while left < right:
                if text[left] != text[right]:
                    return False
                left += 1
                right -= 1
            return True

        for right in range(len(text) - 1, -1, -1):
            if isPalindrome(0, right):
                return "".join(reversed(text[right + 1: ])) + text
        return ""


print(Solution().shortestPalindrome("bc") == "cbc")
print(Solution().shortestPalindrome("aacecaaa") == "aaacecaaa")
print(Solution().shortestPalindrome("abcd") == "dcbabcd")
print(Solution().shortestPalindrome("") == "")
