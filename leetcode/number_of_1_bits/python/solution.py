class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, bit mask
        """
        counter = 0
        for index in range(0, 32):
            counter += bool(num & 2**index)
        return counter


class Solution:
    def hammingWeight(self, number: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        set_bit_counter = 0

        while number:
            set_bit_counter += number % 2
            number = number // 2

        return set_bit_counter


class Solution:
    def hammingWeight(self, number: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation, bit mask
        """
        set_bit_counter = 0

        while number:
            set_bit_counter += number & 1
            number = number >> 1

        return set_bit_counter


class Solution:
    def hammingWeight(self, number: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(n)
        Tags: bit manipulation, build-in function
        """
        return bin(number).count("1")


class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, bit mask
        """
        counter = 0
        mask = 1
        for _ in range(0, 32):
            if mask & num:
                counter += 1
            mask <<= 1
        return counter


print(Solution().hammingWeight(0) == 0)
print(Solution().hammingWeight(1) == 1)
print(Solution().hammingWeight(2) == 1)
print(Solution().hammingWeight(3) == 2)
print(Solution().hammingWeight(4) == 1)
print(Solution().hammingWeight(11) == 3)
print(Solution().hammingWeight(128) == 1)
print(Solution().hammingWeight(2147483645) == 30)
