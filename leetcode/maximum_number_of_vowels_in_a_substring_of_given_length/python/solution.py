class Solution:
    def maxVowels(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        window_vovel_count = 0
        vovels = "aeiou"
        max_vovels = 0

        for right, letter in enumerate(text):
            if letter in vovels:
                window_vovel_count += 1
            
            if right - left + 1 == k:
                max_vovels = max(max_vovels, window_vovel_count)

                left_letter = text[left]
                if left_letter in vovels:
                    window_vovel_count -= 1
                left += 1

        return max_vovels


print(Solution().maxVowels("abciiidef", 3) == 3)
print(Solution().maxVowels("aeiou", 2) == 2)
print(Solution().maxVowels("leetcode", 3) == 2)