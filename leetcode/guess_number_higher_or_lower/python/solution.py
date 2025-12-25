class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: 
            A: binary search
        """
        def guess(number: int) -> int:
            if number == 6:
                return 0
            elif number > 6:
                return -1
            else:
                return 1
        
        left = 1
        right = n

        while left <= right:
            middle = left + (right - left) // 2
            guessed = guess(middle)
            
            if guessed == 0:
                return middle
            elif guessed == - 1:
                right = middle - 1
            else:
                left = middle + 1


print(Solution().guessNumber(10) == 6)
