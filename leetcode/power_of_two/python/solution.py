class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        if n <= 0:
            return False

        while n % 2 == 0:
            n >>= 1

        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: recursion
        """
        if n <= 0:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n >> 1)
        else:
            return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        return n > 0 and (n & (n - 1)) == 0


print(Solution().isPowerOfTwo(1) == True)
print(Solution().isPowerOfTwo(16) == True)
print(Solution().isPowerOfTwo(3) == False)
print(Solution().isPowerOfTwo(-4) == False)
print(Solution().isPowerOfTwo(0) == False)
