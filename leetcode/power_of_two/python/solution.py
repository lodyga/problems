class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        return n > 0 and (n & (n - 1)) == 0


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, iteration
        """
        if n <= 0:
            return False

        while n != 1:
            if n & 1:
                return False
            n >>= 1

        return True


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
            n //= 2

        return n == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: recursion
        """
        if n <= 0:
            return False
        elif n % 2:
            return n == 1
        else:
            return self.isPowerOfTwo(n // 2)


print(Solution().isPowerOfTwo(1) == True)
print(Solution().isPowerOfTwo(16) == True)
print(Solution().isPowerOfTwo(3) == False)
print(Solution().isPowerOfTwo(-4) == False)
print(Solution().isPowerOfTwo(0) == False)
