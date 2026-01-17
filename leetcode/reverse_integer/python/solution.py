import math


class Solution:
    def reverse(self, x: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        MIN = -2**31  # -2_147_483_648
        MAX = 2**31 - 1  # 2_147_483_647
        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                res > MAX // 10 or
                res == MAX // 10 and digit > MAX % 10
            ):
                return 0
            elif (
                res < MIN // 10 or
                res == MIN // 10 and digit < MIN % 10
            ):
                return 0

            res = (res * 10) + digit

        return res


print(Solution().reverse(123) == 321)
print(Solution().reverse(-123) == -321)
print(Solution().reverse(120) == 21)
print(Solution().reverse(-1563847412) == 0)
