class Solution:
    def maximumOddBinaryNumber(self, num: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, string
            A: iteration
        """
        odd = 0
        for digit in num:
            if digit == "1":
                odd += 1

        res = ["0"] * len(num)
        res[-1] = "1"
        for index in range(odd - 1):
            res[index] = "1"

        return "".join(res)


class Solution:
    def maximumOddBinaryNumber(self, num: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        odd = 0
        for digit in num:
            if digit == "1":
                odd += 1
        even = len(num) - odd

        return "1"*(odd - 1) + "0"*(even) + "1"


print(Solution().maximumOddBinaryNumber("1") == "1")
print(Solution().maximumOddBinaryNumber("10") == "01")
print(Solution().maximumOddBinaryNumber("010") == "001")
print(Solution().maximumOddBinaryNumber("0101") == "1001")
