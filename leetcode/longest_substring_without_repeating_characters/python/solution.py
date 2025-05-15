class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window as hash set
        """
        window = set()
        longest_substring = 1
        left = 0

        for right, letter in enumerate(word):
            while letter in window:
                window.remove(word[left])
                left += 1
            else:
                window.add(letter)
                longest_substring = max(longest_substring, right - left + 1)

        return longest_substring


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


print(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
print(Solution().lengthOfLongestSubstring("bbbbb"), 1)
print(Solution().lengthOfLongestSubstring("pwwkew"), 3)
print(Solution().lengthOfLongestSubstring("aabaab!bb"), 3)
print(Solution().lengthOfLongestSubstring("aab"), 2)