class Solution:
    def longestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        res_len = 1
        res_start = 0

        def get_palindrome_len(idx: int, d: int) -> int:
            left = idx
            right = idx + d

            while (
                left > -1 and right < len(text) and
                text[left] == text[right]
            ):
                left -= 1
                right += 1

            return right - left - 1

        # Check for odd length palindrome.
        for idx in range(1, len(text) - 1):
            pal_len = get_palindrome_len(idx, 0)

            if pal_len > res_len:
                res_len = pal_len
                res_start = idx - res_len // 2

        # Check for even length palindrome.
        for idx in range(len(text) - 1):
            pal_len = get_palindrome_len(idx, 1)

            if pal_len > res_len:
                res_len = pal_len
                res_start = idx - res_len // 2 + 1

        return text[res_start: res_start + res_len]


class Solution:
    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def longestPalindrome(self, word: str) -> str:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        palindrome = ""
        palindrome_length = 0

        for left in range(len(word)):
            for right in range(left, len(word)):
                if self.is_palindrome(word[left: right + 1]):
                    if right - left + 1 > palindrome_length:
                        palindrome = word[left: right + 1]
                        palindrome_length = right - left + 1

        return palindrome


print(Solution().longestPalindrome("babad") == "bab")
print(Solution().longestPalindrome("cbbd") == "bb")
print(Solution().longestPalindrome("a") == "a")
print(Solution().longestPalindrome("bb") == "bb")
print(Solution().longestPalindrome("ab") == "a")
print(Solution().longestPalindrome("aacabdkacaa") == "aca")
print(Solution().longestPalindrome("abdka") == "a")
print(Solution().longestPalindrome("aaaa") == "aaaa")
