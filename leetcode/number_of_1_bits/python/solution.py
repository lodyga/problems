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
            number = number >> 1

        return set_bit_counter


class Solution:
    def hammingWeight(self, number: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(n)
        Tags: bit manipulation
        """
        return bin(number).count("1")


    def hammingWeight(self, number: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        set_bit_counter = 0
        
        while number:
            set_bit_counter += number & 1
            number = number >> 1

        return set_bit_counter


print(Solution().hammingWeight(0) == 0)
print(Solution().hammingWeight(1) == 1)
print(Solution().hammingWeight(2) == 1)
print(Solution().hammingWeight(3) == 2)
print(Solution().hammingWeight(4) == 1)
print(Solution().hammingWeight(11) == 3)
print(Solution().hammingWeight(128) == 1)
print(Solution().hammingWeight(2147483645) == 30)