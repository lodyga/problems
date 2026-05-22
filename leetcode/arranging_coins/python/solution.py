class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            coin_count = (1 + mid) * mid // 2

            if n == coin_count:
                return mid
            elif n < coin_count:
                right = mid - 1
            else:
                left = mid + 1

        return right


print(Solution().arrangeCoins(5) == 2)
print(Solution().arrangeCoins(8) == 3)
print(Solution().arrangeCoins(1) == 1)
print(Solution().arrangeCoins(2) == 1)
print(Solution().arrangeCoins(3) == 2)
print(Solution().arrangeCoins(4) == 2)
print(Solution().arrangeCoins(6) == 3)
print(Solution().arrangeCoins(1804289383) == 60070)
