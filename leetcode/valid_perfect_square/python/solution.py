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
            mid = (left + right) // 2
            squared = mid**2

            if squared == square:
                return True
            elif squared > square:
                right = mid - 1
            else:
                left = mid + 1

        return False


print(Solution().isPerfectSquare(16) == True)
print(Solution().isPerfectSquare(14) == False)
