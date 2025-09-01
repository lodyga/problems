class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


print(Solution().getSum(1, 2), 3)
print(Solution().getSum(2, 3), 5)
print(Solution().getSum(-1, 1), 0)
print(Solution().getSum(-12, -8), -20)