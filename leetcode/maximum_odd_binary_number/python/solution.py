class Solution:
    def maximumOddBinaryNumber(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, string
            A: iteration
        """
        bin_freq = [0, 0]

        for chr in text:
            if chr == "0":
                bin_freq[0] += 1
            else:
                bin_freq[1] += 1

        return (
            "1" * (bin_freq[1] - 1)
            + "0" * bin_freq[0]
            + "1"
        )


class Solution:
    def maximumOddBinaryNumber(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        odd = 0
        for chr in text:
            if chr == "1":
                odd += 1
        even = len(text) - odd

        return "1"*(odd - 1) + "0"*(even) + "1"


print(Solution().maximumOddBinaryNumber("1") == "1")
print(Solution().maximumOddBinaryNumber("10") == "01")
print(Solution().maximumOddBinaryNumber("010") == "001")
print(Solution().maximumOddBinaryNumber("0101") == "1001")
