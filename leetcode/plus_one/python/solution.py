class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: iteration
        """
        carry = True
        index = len(digits) - 1
        
        while index > -1 and carry:
            if digits[index] == 9:
                carry = True
                digits[index] = 0
            else:
                carry = False
                digits[index] += 1
            index -= 1

        if carry:
            digits.insert(0, 1)
        
        return digits


print(Solution().plusOne([1, 2, 3]) == [1, 2, 4])
print(Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
print(Solution().plusOne([9]) == [1, 0])
print(Solution().plusOne([9, 9]) == [1, 0, 0])