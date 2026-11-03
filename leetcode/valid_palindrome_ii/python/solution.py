class Solution:
    def validPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        def isPalindrome(left: int, right: int, joker: bool) -> bool:
            while left < right:
                if text[left] == text[right]:
                    left += 1
                    right -= 1
                elif joker:
                    return (
                        isPalindrome(left + 1, right, False)
                        or isPalindrome(left, right - 1, False)
                    )
                else:
                    return False

            return True

        return isPalindrome(0, len(text) - 1, True)


print(Solution().validPalindrome("aba") is True)
print(Solution().validPalindrome("abca") is True)
print(Solution().validPalindrome("abc") is False)
print(Solution().validPalindrome("deeee") is True)
print(Solution().validPalindrome("eeccccbebaeeabebccceea") is False)
print(Solution().validPalindrome("abzzbab") is True)
print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") is True)
