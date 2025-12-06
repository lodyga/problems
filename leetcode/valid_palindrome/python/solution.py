class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0
        right = len(text) - 1

        while left < right:
            while (
                left < right and
                text[left].isalnum() is False
            ):
                left += 1
            while (
                left < right and
                text[right].isalnum() is False
            ):
                right -= 1
            if text[left].lower() != text[right].lower():
                return False
            left += 1
            right -= 1

        return True


class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: two pointers, build-in function
        """
        joined = "".join(filter(str.isalnum, text)).lower()
        return joined == joined[::-1]


import string
class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, build-in function
        """
        left = 0
        right = len(text) - 1
        while left < right:
            while left < right and text[left] in string.punctuation:
                left += 1
            while left < right and text[right] in string.punctuation:
                right -= 1
            if text[left].lower() != text[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


import re
class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: two pointers, build-in function
        """
        cleaned_text = re.sub(r"[\W_]", "", text).lower()
        return cleaned_text == cleaned_text[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama") == True)
print(Solution().isPalindrome("race a car") == False)
print(Solution().isPalindrome(" ") == True)
print(Solution().isPalindrome("0P") == False)
print(Solution().isPalindrome("ab_a") == True)
print(Solution().isPalindrome("a,,") == True)
