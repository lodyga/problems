class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        N = len(bits)
        index = 0
        is_one_bit = True

        while index < N:
            if bits[index]:
                is_one_bit = False
                index += 2
            else:
                is_one_bit = True
                index += 1

        return is_one_bit


print(Solution().isOneBitCharacter([1, 0, 0]) == True)
print(Solution().isOneBitCharacter([1, 1, 1, 0]) == False)
print(Solution().isOneBitCharacter([0, 0]) == True)
