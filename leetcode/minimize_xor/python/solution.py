class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        def count_bits(num):
            set_bits = 0
            while num:
                set_bits += num & 1
                num >>= 1
            return set_bits

        bit_count1 = count_bits(num1)
        bit_count2 = count_bits(num2)
        index = 0

        # Remove least significant bits.
        while bit_count1 > bit_count2:
            if num1 & (1 << index):
                num1 ^= (1 << index)
                bit_count1 -= 1
            index += 1

        # Add least significant bits.
        while bit_count1 < bit_count2:
            if num1 & (1 << index) == 0:
                num1 |= (1 << index)
                # num1 ^= (1 << index)
                bit_count1 += 1
            index += 1

        return num1


print(Solution().minimizeXor(3, 5) == 3)
print(Solution().minimizeXor(1, 12) == 3)
print(Solution().minimizeXor(65, 84) == 67)
