class Solution:
    def maxVowels(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: string
            A: sliding window
        """
        VOWELS = "aeiou"
        vowel_window = 0
        left = 0
        vowel_counter = 0

        for right, letter in enumerate(text):
            vowel_window += letter in VOWELS
            
            if right + 1 < k:
                continue

            vowel_counter = max(vowel_counter, vowel_window)
            left_letter = text[left]
            vowel_window -= left_letter in VOWELS
            left+= 1

        return vowel_counter


print(Solution().maxVowels("abciiidef", 3) == 3)
print(Solution().maxVowels("aeiou", 2) == 2)
print(Solution().maxVowels("leetcode", 3) == 2)
