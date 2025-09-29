"""
draft
7 -> 49 -> 16 + 81 -> 97, 81 + 49 = 130 -> 1 + 9 = 10 -> 1
2 -> 4, 16 -> 1 + 36 = 37 -> 9 + 49 = 58 -> 25 + 64 = 89 -> 64 + 81 = 145 -> 1 + 16 + 25 = 42 -> 16 + 4 = 20
"""


class Solution:
    def isHappy(self, number: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: hash set
        """
        prev_numbers = set([number])

        while True:
            number = sum(int(digit)**2 for digit in str(number))

            if number == 1:
                return True
            elif number in prev_numbers:
                return False
            else:
                prev_numbers.add(number)


class Solution:
    def isHappy(self, number: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: hash set
        """
        def sum_of_squares(number):
            new_number = 0
            while number:
                new_number += (number % 10)**2
                number //= 10
            return new_number

        prev_numbers = set()

        while number not in prev_numbers:
            prev_numbers.add(number)
            number = sum_of_squares(number)

            if number == 1:
                return True
            
        return False


print(Solution().isHappy(19) == True)
print(Solution().isHappy(2) == False)
print(Solution().isHappy(7) == True)
print(Solution().isHappy(100) == True)
print(Solution().isHappy(101) == False)