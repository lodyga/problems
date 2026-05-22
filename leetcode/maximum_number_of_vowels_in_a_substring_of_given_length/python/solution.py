class Solution:
    def maxVowels(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: sliding window
        """
        VOWELS = "aeoiu"
        vowel_window = 0
        res = 0

        for right, letter in enumerate(text):
            if letter in VOWELS:
                vowel_window += 1

            if right >= k - 1:
                res = max(res, vowel_window)

                if text[right - k + 1] in VOWELS:
                    vowel_window -= 1

        return res


print(Solution().maxVowels("abciiidef", 3) == 3)
print(Solution().maxVowels("aeiou", 2) == 2)
print(Solution().maxVowels("leetcode", 3) == 2)
