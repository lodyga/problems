class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: greedy
        """
        digit_num = list(str(num))

        for index in range(len(digit_num)):
            if digit_num[index] == "6":
                digit_num[index] = "9"
                break

        return int("".join(digit_num))


print(Solution().maximum69Number(9669) == 9969)
print(Solution().maximum69Number(9996) == 9999)
print(Solution().maximum69Number(9999) == 9999)
