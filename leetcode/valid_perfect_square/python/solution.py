class Solution:
    def isPerfectSquare(self, square: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 1
        right = square

        while left <= right:
            middle = left + (right - left) // 2
            curr_square = middle**2

            if curr_square == square:
                return True
            elif curr_square > square:
                right = middle - 1
            else:
                left = middle + 1

        return False


print(Solution().isPerfectSquare(16) == True)
print(Solution().isPerfectSquare(14) == False)
