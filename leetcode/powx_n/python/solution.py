class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: recursion
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            # base = self.myPow(x, n // 2)
            base = self.myPow(x, n >> 1)
            # return base**2 * (x if n % 2 else 1)
            return base * base * (x if n & 1 else 1)


print(Solution().myPow(2, 10), 1024)
print(Solution().myPow(2.1, 3), 9.261)
print(Solution().myPow(2, -2), 0.25)
print(Solution().myPow(2, -200000000), 0)
print(Solution().myPow(0.00001, 2147483647), 0)
print(Solution().myPow(2.00000, -2147483648), 0)