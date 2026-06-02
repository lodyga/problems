class Solution:
    def equalSubstring(self, text1: str, text2: str, max_cost: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        left = 0
        res = 0

        for right, (letter1, letter2) in enumerate(zip(text1, text2)):
            cost = abs(ord(letter1) - ord(letter2))
            max_cost -= cost

            while max_cost < 0:
                cost = abs(ord(letter1) - ord(letter2))
                max_cost += cost
                left += 1

            res = max(res, right - left + 1)

        return res


print(Solution().equalSubstring("abcd", "bcdf", 3) == 3)
print(Solution().equalSubstring("abcd", "cdef", 3) == 1)
print(Solution().equalSubstring("abcd", "acde", 0) == 1)
