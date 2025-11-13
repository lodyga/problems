class Solution:
    def minimizeXor(self, number1: int, number2: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        def count_bits(number):
            set_bits = 0
            while number:
                set_bits += number & 1
                number >>= 1
            return set_bits

        bit_count1 = count_bits(number1)
        bit_count2 = count_bits(number2)
        index = 0

        # remove least significant bits
        while bit_count1 > bit_count2:
            if number1 & (1 << index):
                bit_count1 -= 1
                number1 ^= (1 << index)
            index += 1

        # add least significant bits
        while bit_count1 < bit_count2:
            if number1 & (1 << index) == 0:
                bit_count1 += 1
                number1 |= (1 << index)
            index += 1

        return number1


print(Solution().minimizeXor(3, 5) == 3)
print(Solution().minimizeXor(1, 12) == 3)
