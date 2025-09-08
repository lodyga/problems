# 7&8&9&10 #  0
# 9&10  # 8

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        bitwise_and = right
        for number in range(left, right):
            bitwise_and &= number
        return bitwise_and


print(Solution().rangeBitwiseAnd(5, 7), 4)
print(Solution().rangeBitwiseAnd(0, 0), 0)
print(Solution().rangeBitwiseAnd(0, 2147483647), 0)