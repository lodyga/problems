# 4 & 5 & 6  # 4
# 4 & 7 & 13  # 4


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation, tle
        """
        last = x
        for _ in range(n - 1):
            last = (last + 1) | x
        return last


print(Solution().minEnd(3, 4), 6)
print(Solution().minEnd(2, 7), 15)
print(Solution().minEnd(3, 5), 13)
print(Solution().minEnd(3, 5), 13)
print(Solution().minEnd(69735293, 5563569), 142821814265)