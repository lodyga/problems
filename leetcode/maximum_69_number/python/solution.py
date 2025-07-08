class Solution:
    def maximum69Number(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        digit_array = list(str(number))
        
        for index, digit in enumerate(digit_array):
            if digit == "6":
                digit_array[index] = "9"
                return int("".join(digit_array))

        return number


print(Solution().maximum69Number(9669) == 9969)
print(Solution().maximum69Number(9996) == 9999)
print(Solution().maximum69Number(9999) == 9999)