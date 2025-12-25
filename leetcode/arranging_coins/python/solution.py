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
            middle = left + (right - left) // 2
            coin_count = (1 + middle) * middle // 2

            if coin_count == n:
                return middle
            elif coin_count > n:
                right = middle - 1
            else:
                left = middle + 1

        return right


print(Solution().arrangeCoins(1) == 1)
print(Solution().arrangeCoins(2) == 1)
print(Solution().arrangeCoins(3) == 2)
print(Solution().arrangeCoins(4) == 2)
print(Solution().arrangeCoins(5) == 2)
print(Solution().arrangeCoins(6) == 3)
print(Solution().arrangeCoins(8) == 3)
print(Solution().arrangeCoins(1804289383) == 60070)
