class Solution:
    def __init__(self):
        self.palindrome_counter = 0

    def countSubstrings(self, word: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def countPalindromes(left, right):
            while (left >= 0 and
                right < len(word) and
                    word[left] == word[right]):
                self.palindrome_counter += 1
                left -= 1
                right += 1

        for index in range(len(word)):
            # check for odd length palindromes
            countPalindromes(index, index)
            # check for even length palindromes
            countPalindromes(index, index + 1)

        return self.palindrome_counter


print(Solution().countSubstrings("abc") == 3)
print(Solution().countSubstrings("aaa") == 6)
