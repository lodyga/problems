# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = n

        while left <= right:
            middle_number = (left + right) // 2
            guess_val = self.guess(middle_number)
            
            if guess_val == 0:
                return middle_number
            elif guess_val == - 1:
                right = middle_number - 1
            else:
                left = middle_number + 1

    def guess(self, number: int) -> int:
        if number == 6:
            return 0
        elif number > 6:
            return -1
        else:
            return 1


print(Solution().guessNumber(10), 6)