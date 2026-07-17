class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        res = 0

        while num:
            res += num & 1
            num >>= 1

        return res


class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        res = 0

        while num:
            res += num % 2
            num //= 2

        return res


class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(n)
        Tags:
            A: bit manipulation, built-in function
        """
        return bin(num).count("1")


class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, bit mask
        """
        res = 0
        mask = 1

        for _ in range(32):
            if num & mask:
                res += 1

            mask <<= 1

        return res


print(Solution().hammingWeight(1) == 1)
print(Solution().hammingWeight(2) == 1)
print(Solution().hammingWeight(2147483645) == 30)
print(Solution().hammingWeight(0) == 0)
print(Solution().hammingWeight(3) == 2)
print(Solution().hammingWeight(4) == 1)
print(Solution().hammingWeight(11) == 3)
print(Solution().hammingWeight(128) == 1)
