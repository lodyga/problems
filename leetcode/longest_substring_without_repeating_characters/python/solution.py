class Solution:
    def lengthOfLongestSubstring(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash set
            A: sliding window
        """
        window_letters = set()
        substring_lenght = 0
        left = 0

        for right, letter in enumerate(text):
            while letter in window_letters:
                left_letter = text[left]
                window_letters.discard(left_letter)
                left += 1

            window_letters.add(letter)
            substring_lenght = max(substring_lenght, right - left + 1)

        return substring_lenght


class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        longest_substring = 1

        for left in range(len(word)):
            for right in range(left, len(word)):
                substring = word[left: right + 1]

                if len(substring) == len(set(substring)):
                    longest_substring = max(
                        longest_substring,
                        right - left + 1)

        return longest_substring


print(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
print(Solution().lengthOfLongestSubstring("bbbbb") == 1)
print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
print(Solution().lengthOfLongestSubstring("aabaab!bb") == 3)
print(Solution().lengthOfLongestSubstring("aab") == 2)
