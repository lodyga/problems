class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp
        """
        BASE = 29
        MOD = 10**9 + 7
        prefix = 0
        suffix = 0
        power = 1
        last_index = 0

        for index, letter in enumerate(text):
            value = (ord(letter) - ord("a"))
            prefix = (prefix*BASE + value) % MOD
            suffix = (suffix + value*power) % MOD
            power = (power * BASE) % MOD

            if prefix == suffix:
                last_index = index

        return text[last_index + 1:][::-1] + text


class Solution:
    def shortestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers, tle
        """
        def isPalindrome(left, right):
            while left < right:
                if text[left] != text[right]:
                    return False
                left += 1
                right -= 1
            return True
        

        missing = []
        for right in reversed(range(len(text))):
            if isPalindrome(0, right):
                return "".join(missing) + text
            missing.append(text[right])
        return ""


class Solution:
    def shortestPalindrome(self, text: str) -> str:
        def get_letter_value(char):
            return ord(char) - ord("a")

        BASE = 29
        MOD = 10**9 + 7

        straight_hash = 0
        power = BASE**(len(text) - 1)
        for letter_index in range(len(text)):
            straight_hash = (straight_hash + get_letter_value(text[letter_index]) * power) % MOD
            power //= BASE

        reversed_hash = 0
        power = 1
        for index in range(len(text)):
            reversed_hash = (reversed_hash + get_letter_value(text[index]) * power) % MOD
            power *= BASE

        missing = []
        power = BASE**(len(text) - 1)
        for right in reversed(range(len(text))):
            if straight_hash == reversed_hash:
                return "".join(missing) + text
            missing.append(text[right])

            straight_hash -= get_letter_value(text[right])
            if straight_hash < 0:
                straight_hash += MOD
            straight_hash //= BASE
            reversed_hash -= get_letter_value(text[right]) * power
            power //= BASE
            if reversed_hash < 0:
                reversed_hash += MOD

        return ""


print(Solution().shortestPalindrome("bc") == "cbc")
print(Solution().shortestPalindrome("aacecaaa") == "aaacecaaa")
print(Solution().shortestPalindrome("abcd") == "dcbabcd")
print(Solution().shortestPalindrome("") == "")