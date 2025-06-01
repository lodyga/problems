class Solution:
    def equalSubstring(self, word1: str, word2: str, max_cost: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        window_length = 0

        for right, (letter1, letter2) in enumerate(zip(word1, word2)):
            max_cost -= abs(ord(letter1) - ord(letter2))

            while max_cost < 0:
                max_cost += abs(ord(word1[left]) - ord(word2[left]))
                left += 1
            
            window_length = max(window_length, right - left + 1)
        
        return window_length


print(Solution().equalSubstring("abcd", "bcdf", 3) == 3)
print(Solution().equalSubstring("abcd", "cdef", 3) == 1)
print(Solution().equalSubstring("abcd", "acde", 0) == 1)