class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        if left == right:
            return 0

        res = right
        for num in range(left, right):
            res &= num
        return res


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        res = 0

        for index in range(32):
            bit = (left >> index) & 1
            if bit == 0:
                continue

            remainder = left % (1 << index + 1)
            diff = (1 << index + 1) - remainder

            if right - left < diff:
                res |= 1 << index

        return res


print(Solution().rangeBitwiseAnd(5, 7) == 4)
print(Solution().rangeBitwiseAnd(0, 0) == 0)
print(Solution().rangeBitwiseAnd(1, 2) == 0)
print(Solution().rangeBitwiseAnd(416, 436) == 416)
print(Solution().rangeBitwiseAnd(0, 2147483647) == 0)
print(Solution().rangeBitwiseAnd(2147483646, 2147483647) == 2147483646)
