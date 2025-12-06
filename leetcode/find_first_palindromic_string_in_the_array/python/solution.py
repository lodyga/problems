class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        Time complexity: O(n*k)
            k: word count
            n: avg word length
        Auxiliary space complexity: O(1)
        Tags: 
            A: two pointers
        """
        def is_palindrome(word: str) -> bool:
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""


    def firstPalindrome(self, words: list[str]) -> str:
        """
        Time complexity: O(n*k)
            k: word count
            n: avg word length
        Auxiliary space complexity: O(k)
        Tags: 
            A: two pointers, build-in function
        """
        for word in words:
            if word == "".join(reversed(word)):
                return word
        return ""


print(Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada")
print(Solution().firstPalindrome(["notapalindrome", "racecar"]) == "racecar")
print(Solution().firstPalindrome(["def", "ghi"]) == "")
print(Solution().firstPalindrome(["cqllrtyhw", "swwisru", "gpzmbders", "wqibjuqvs", "pp", "usewxryy", "ybqfuh", "hqwwqftgyu", "jggmatpk"]) == "pp")
