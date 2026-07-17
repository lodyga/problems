r"""
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 14
   |  |__|   |
   |_________|

"""


class Solution:
    def checkPerfectNumber(self, target: int) -> bool:
        """
        Time complexity: O(sqrtn)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        if target == 1:
            return False

        divisor_sum = 1

        for divisor in range(2, int(target**0.5) + 1):
            if target % divisor == 0:
                divisor_sum += divisor
                divisor_sum += target // divisor

        return target == divisor_sum


print(Solution().checkPerfectNumber(28) == True)
print(Solution().checkPerfectNumber(7) == False)
print(Solution().checkPerfectNumber(6) == True)
print(Solution().checkPerfectNumber(1) == False)
print(Solution().checkPerfectNumber(99999996) == False)
