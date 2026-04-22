class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        res = 0

        while n > 1:
            res += n // 2
            n = (n + 1) // 2

        return res


print(Solution().numberOfMatches(7) == 6)
print(Solution().numberOfMatches(14) == 13)
