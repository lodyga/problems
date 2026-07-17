class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        str_num = list(str(num))

        for idx, char in enumerate(str_num):
            if char == "6":
                str_num[idx] = "9"
                break

        return int("".join(str_num))


print(Solution().maximum69Number(9669) == 9969)
print(Solution().maximum69Number(9996) == 9999)
print(Solution().maximum69Number(9999) == 9999)
