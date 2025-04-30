class Solution:
    def validPalindrome(self, word: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def is_valid_palindrome(left: str, right: str) -> bool:
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return is_valid_palindrome(left + 1, right) or \
                    is_valid_palindrome(left, right - 1)

        return True


class Solution:
    def validPalindrome(self, word: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def is_valid_palindrome(left: str, right: str, joker: bool) -> bool:
            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    if joker:
                        return is_valid_palindrome(left + 1, right, False) or \
                            is_valid_palindrome(left, right - 1, False)
                    else:
                        return False

            return True

        return is_valid_palindrome(0, len(word) - 1, True)


print(Solution().validPalindrome("aba") == True)
print(Solution().validPalindrome("abca") == True)
print(Solution().validPalindrome("abc") == False)
print(Solution().validPalindrome("deeee") == True)
print(Solution().validPalindrome("eeccccbebaeeabebccceea") == False)
print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True)
