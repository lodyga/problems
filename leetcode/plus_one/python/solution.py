class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        digits.reverse()
        carry = 1

        for index, digit in enumerate(digits):
            digit += carry
            carry = 0
            if digit == 10:
                digit = 0
                carry = 1
            digits[index] = digit

        if carry:
            digits.append(1)

        digits.reverse()
        return digits


print(Solution().plusOne([1, 2, 3]) == [1, 2, 4])
print(Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
print(Solution().plusOne([9]) == [1, 0])
print(Solution().plusOne([9, 9]) == [1, 0, 0])
