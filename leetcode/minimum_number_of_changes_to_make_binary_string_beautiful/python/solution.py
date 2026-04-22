class Solution:
    def minChanges(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, counting
        """
        return sum(1 for index in range(0, len(s), 2)
                   if s[index] != s[index + 1])


print(Solution().minChanges("10") == 1)
print(Solution().minChanges("1001") == 2)
print(Solution().minChanges("0000") == 0)
print(Solution().minChanges("100100") == 2)
print(Solution().minChanges("100111") == 2)
