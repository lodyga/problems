class Solution:
    def validPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: two pointers
        """
        def validate(left: int, right: int, joker: bool) -> bool:
            while left < right:
                if text[left] == text[right]:
                    left += 1
                    right -= 1
                elif joker:
                    return (
                        validate(left + 1, right, False) or
                        validate(left, right - 1, False)
                    )
                else:
                    return False
            return True

        return validate(0, len(text) - 1, True)


print(Solution().validPalindrome("aba") == True)
print(Solution().validPalindrome("abca") == True)
print(Solution().validPalindrome("abc") == False)
print(Solution().validPalindrome("deeee") == True)
print(Solution().validPalindrome("eeccccbebaeeabebccceea") == False)
print(Solution().validPalindrome("abzzbab") == True)
print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True)
