class Solution:
    def equalSubstring(self, text1: str, text2: str, max_cost: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        left = 0
        max_lenght = 0

        for right, (letter1, letter2) in enumerate(zip(text1, text2)):
            max_cost -= abs(ord(letter1) - ord(letter2))

            while max_cost < 0:
                max_cost += abs(ord(text1[left]) - ord(text2[left]))
                left += 1

            max_lenght = max(max_lenght, right - left + 1)

        return max_lenght


print(Solution().equalSubstring("abcd", "bcdf", 3) == 3)
print(Solution().equalSubstring("abcd", "cdef", 3) == 1)
print(Solution().equalSubstring("abcd", "acde", 0) == 1)
