# 49, 16 + 81 = 97, 81 + 49 = 130, 1 + 9 = 10,


class Solution:
    def isHappy(self, number: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: hash set
        """
        visited = set([number])

        while True:
            number = sum(int(digit)**2 for digit in str(number))

            if number == 1:
                return True

            if number in visited:
                return False
            else:
                visited.add(number)


class Solution:
    def isHappy(self, number: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: hash set
        """
        visited = set()

        def sum_of_squares(number):
            new_number = 0
            while number:
                new_number += (number % 10)**2
                number //= 10
            return new_number

        while number not in visited:
            visited.add(number)
            # number = sum(int(digit)**2 for digit in str(number))
            number = sum_of_squares(number)

            if number == 1:
                return True
        
        return False


print(Solution().isHappy(19), True)
print(Solution().isHappy(2), False)
print(Solution().isHappy(7), True)