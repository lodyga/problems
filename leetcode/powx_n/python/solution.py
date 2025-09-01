class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: recursion
        """
        def dfs(n):
            if n == 0:
                return 1
            else:
                number = dfs(n // 2)
                return number * number * (x if n % 2 else 1)
        
        return dfs(n) if n > 0 else (1 / dfs(-n))


print(Solution().myPow(2, 10), 1024)
print(Solution().myPow(2.1, 3), 9.261)
print(Solution().myPow(2, -2), 0.25)
print(Solution().myPow(2, -200000000), 0)
print(Solution().myPow(0.00001, 2147483647), 0)