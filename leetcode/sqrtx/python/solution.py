class Solution:
    def mySqrt(self, X: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: 
            A: binary search
        """
        left = 1
        right = X
        res = X

        while left <= right:
            middle = left + (right - left) // 2
            square = middle*middle

            if square == X:
                return middle
            elif square < X:
                res = middle
                left = middle + 1
            else:
                right = middle - 1

        return res


print(Solution().mySqrt(4) == 2)
print(Solution().mySqrt(8) == 2)
