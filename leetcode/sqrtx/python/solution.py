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
            mid = (left + right) // 2
            squared = mid**2

            if squared == X:
                return mid
            elif squared < X:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


print(Solution().mySqrt(4) == 2)
print(Solution().mySqrt(8) == 2)
