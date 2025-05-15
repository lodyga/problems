class Solution:
    def __init__(self):
        self.start = 0
        self.palindrome_length = 0

    def longestPalindrome(self, word: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def check_for_palindrome(left, right):
            while (left >= 0 and
                   right < len(word) and
                   word[left] == word[right]):
                if right - left + 1 > self.palindrome_length:
                    self.palindrome_length = right - left + 1
                    self.start = left

                left -= 1
                right += 1

        for index in range(len(word)):
            # check for odd length palindrome
            check_for_palindrome(index, index)
            # check for even length palindrome
            check_for_palindrome(index, index + 1)

        return word[self.start: self.start + self.palindrome_length]


class Solution:
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


print(Solution().longestPalindrome("babad"), "bab")
print(Solution().longestPalindrome("cbbd"), "bb")
print(Solution().longestPalindrome("a"), "a")
print(Solution().longestPalindrome(""), "")
print(Solution().longestPalindrome("bb"), "bb")
print(Solution().longestPalindrome("ab"), "a")
print(Solution().longestPalindrome("aacabdkacaa"), "aca")
print(Solution().longestPalindrome("abdka"), "a")
print(Solution().longestPalindrome("aaaa"), "aaaa")