class Solution:
    def longestPalindrome(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        def check_for_palindrome(left, right):
            nonlocal start, palindrome_length, longest_palindrome_len
            while (
                left > -1 and
                right < len(text) and
                text[left] == text[right]
            ):
                palindrome_length = right - left + 1
                if palindrome_length > longest_palindrome_len:
                    longest_palindrome_len = palindrome_length
                    start = left
                left -= 1
                right += 1

        start = 0
        palindrome_length = 0
        longest_palindrome_len = 0
        for index in range(len(text)):
            # check for odd length palindrome
            check_for_palindrome(index, index)
            # check for even length palindrome
            check_for_palindrome(index, index + 1)

        return text[start: start + longest_palindrome_len]


class Solution2:
    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def longestPalindrome(self, word: str) -> str:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags: brute-force
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
print(Solution().longestPalindrome("") == "")
print(Solution().longestPalindrome("bb") == "bb")
print(Solution().longestPalindrome("ab") == "a")
print(Solution().longestPalindrome("aacabdkacaa") == "aca")
print(Solution().longestPalindrome("abdka") == "a")
print(Solution().longestPalindrome("aaaa") == "aaaa")
