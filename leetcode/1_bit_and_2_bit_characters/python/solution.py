class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        index = 0
        one_bit = False
        while index < len(bits):
            bit = bits[index]
            if bit:
                index += 2
                one_bit = False
            else:
                index += 1
                one_bit = True

        return one_bit


print(Solution().isOneBitCharacter([1, 0, 0]) == True)
print(Solution().isOneBitCharacter([1, 1, 1, 0]) == False)
print(Solution().isOneBitCharacter([0, 0]) == True)
