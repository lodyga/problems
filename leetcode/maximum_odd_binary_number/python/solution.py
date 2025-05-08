class Solution:
    def maximumOddBinaryNumber(self, number: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        ones = zeros = 0
        
        for digit in number:
            if digit == "1":
                ones += 1
            else:
                zeros += 1

        return "1" * (ones - 1) + "0" * zeros + "1"


print(Solution().maximumOddBinaryNumber("1"), "1")
print(Solution().maximumOddBinaryNumber("10"), "01")
print(Solution().maximumOddBinaryNumber("010"), "001")
print(Solution().maximumOddBinaryNumber("0101"), "1001")