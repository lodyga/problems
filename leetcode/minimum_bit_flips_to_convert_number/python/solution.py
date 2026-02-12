class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        n = start ^ goal
        res = 0

        while n:
            res += n & 1
            n >>= 1

        return res


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        n = start ^ goal
        res = 0

        while n:
            res += 1
            n = n & (n - 1)

        return res


print(Solution().minBitFlips(10, 7) == 3)
print(Solution().minBitFlips(3, 4) == 3)
