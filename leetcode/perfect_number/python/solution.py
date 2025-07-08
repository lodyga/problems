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
        """
        if target == 1:
            return False
        
        divisor_sum = 1
        
        for number in reversed(range(2, int(target ** 0.5) + 1)):
            if target % number == 0:
                divisor_sum += number
                divisor_sum += target // number

        return divisor_sum == target


class Solution:
    def checkPerfectNumber(self, target: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        divisor_sum = 0
        for number in reversed(range(1, target // 2 + 1)):
            if target % number == 0:
                divisor_sum += number

        return divisor_sum == target


print(Solution().checkPerfectNumber(28) == True)
print(Solution().checkPerfectNumber(7) == False)
print(Solution().checkPerfectNumber(6) == True)
print(Solution().checkPerfectNumber(1) == False)
print(Solution().checkPerfectNumber(99999996) == False)