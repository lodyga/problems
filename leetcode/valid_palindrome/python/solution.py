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
            while (left < right and text[left].isalnum() is False):
                left += 1
            
            while (left < right and text[right].isalnum() is False):
                right -= 1
            
            if text[left].lower() == text[right].lower():
                left += 1
                right -= 1
            else:
                return False
            
        return True


class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: build-in function
        """
        joined = "".join(filter(str.isalnum, text)).lower()
        return joined == joined[::-1]


class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, build-in function
        """
        import string
        left = 0
        right = len(text) - 1
        
        while left < right:
            while left < right and text[left] in string.punctuation:
                left += 1
        
            while left < right and text[right] in string.punctuation:
                right -= 1
        
            if text[left].lower() == text[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True


class Solution:
    def isPalindrome(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: build-in function
        """
        import re
        clean_text = re.sub(r"[\W_]", "", text).lower()
        return clean_text == clean_text[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama") == True)
print(Solution().isPalindrome("race a car") == False)
print(Solution().isPalindrome(" ") == True)
print(Solution().isPalindrome("0P") == False)
print(Solution().isPalindrome("ab_a") == True)
print(Solution().isPalindrome("a,,") == True)
