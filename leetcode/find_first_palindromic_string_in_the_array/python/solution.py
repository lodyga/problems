class Solution:
    def firstPalindrome(self, words: list[str]) -> bool:
        """
        Time complexity: O(k*n)
            k: word count
            n: average word length
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""

    def is_palindrome(self, word: str) -> bool:
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1
        
        return True

print(Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"]), "ada")
print(Solution().firstPalindrome(["notapalindrome", "racecar"]), "racecar")
print(Solution().firstPalindrome(["def", "ghi"]), "")