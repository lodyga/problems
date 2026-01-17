class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags:
            A: recursion
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:  # n > 1
            odd_part = x if n % 2 else 1
            base = self.myPow(x, n // 2)
            return base * base * odd_part


print(Solution().myPow(2, 10) == 1024)
print(Solution().myPow(2, 3) == 8)
print(Solution().myPow(2, -2) == 0.25)
print(Solution().myPow(2, -200000000) == 0)
print(Solution().myPow(0.00001, 2147483647) == 0)
print(Solution().myPow(2.00000, -2147483648) == 0)
print(Solution().myPow(0.44528, 0) == 1)
