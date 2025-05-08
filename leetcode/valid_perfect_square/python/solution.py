class Solution:
    def isPerfectSquare(self, square: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = square

        while left <= right:
            side = (left + right) // 2
            current_square = side ** 2

            if current_square == square:
                return True
            elif current_square > square:
                right = side - 1
            else:
                left = side + 1

        return False


print(Solution().isPerfectSquare(16), True)
print(Solution().isPerfectSquare(14), False)