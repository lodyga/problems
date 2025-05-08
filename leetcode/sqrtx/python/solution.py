class Solution:
    def mySqrt(self, suqare: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = suqare

        while left <= right:
            middle = (left + right) // 2
            current_square = middle ** 2

            if current_square == suqare:
                return middle
            elif current_square > suqare:
                right = middle - 1
            else:
                left = middle + 1

        return right


print(Solution().mySqrt(4), 2)
print(Solution().mySqrt(8), 2)