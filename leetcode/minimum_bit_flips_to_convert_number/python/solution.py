class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        counter = 0
        while start or goal:
            if (start & 1) != (goal % 2):
                counter += 1
            start >>= 1
            goal //= 2
        return counter


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        target = start ^ goal
        counter = 0
        while target:
            if target & 1:
                counter += 1
            target >>= 1
        return counter


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        target = start ^ goal
        i = 1
        counter = 0
        while i <= target:
            if target & i:
                counter += 1
            i <<= 1
        return counter


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        n = start ^ goal
        counter = 0
        while n:
            n = n & (n - 1)
            counter += 1
        return counter


print(Solution().minBitFlips(10, 7) == 3)
print(Solution().minBitFlips(3, 4) == 3)