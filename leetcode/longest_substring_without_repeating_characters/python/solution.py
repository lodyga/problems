class Solution:
    def lengthOfLongestSubstring(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, string
            A: sliding window
        """
        char_set = set()
        res = 0
        left = 0
        
        for right, char in enumerate(text):
            while char in char_set:
                char_set.remove(text[left])
                left += 1

            char_set.add(char)
            res = max(res, right - left + 1)

        return res


print(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
print(Solution().lengthOfLongestSubstring("bbbbb") == 1)
print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
print(Solution().lengthOfLongestSubstring("aabaab!bb") == 3)
print(Solution().lengthOfLongestSubstring("aab") == 2)
