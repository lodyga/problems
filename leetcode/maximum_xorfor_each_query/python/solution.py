"""
draft
010 number
xor
101 k
=
111 max number

010 number
xor
111 max number
=
101 k
"""


class Solution:
    def getMaximumXor(self, numbers: list[int], maximumBit: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation, prefix sum
        """
        max_number = (1 << maximumBit) - 1
        max_xor = [max_number] * len(numbers)
        prefix_xor = 0

        for index, number in enumerate(numbers, 1):
            prefix_xor ^= number
            xor = prefix_xor ^ max_number
            max_xor[-index] = xor
        return max_xor


class Solution:
    def getMaximumXor(self, numbers: list[int], maximumBit: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation, prefix sum
        """
        xor = (1 << maximumBit) - 1
        max_xor = [xor] * len(numbers)

        for index, number in enumerate(numbers, 1):
            xor ^= number
            max_xor[-index] = xor
        return max_xor


print(Solution().getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3])
print(Solution().getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5])
print(Solution().getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7])
