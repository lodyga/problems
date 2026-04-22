class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        opened = 0
        opened_added = 0

        for par in s:
            if par == "(":
                opened += 1
            elif opened == 0:
                opened_added += 1
            else:
                opened -= 1

        return opened_added + opened


print(Solution().minAddToMakeValid("())") == 1)
print(Solution().minAddToMakeValid("(((") == 3)
print(Solution().minAddToMakeValid("()))((") == 4)
