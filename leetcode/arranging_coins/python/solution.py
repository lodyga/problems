class Solution:
    def arrangeCoins(self, target: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        total = 0
        level = 0

        while total < target:
            total += total + 1
            level += 1

        return level if total == target else level - 1


class Solution:
    def arrangeCoins(self, coins: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = coins

        while left <= right:
            middle = (left + right) // 2
            coin_count = (1 + middle) * middle / 2

            if coins == coin_count:
                return middle
            elif coins < coin_count:
                right = middle - 1
            else:
                left = middle + 1

        return right


print(Solution().arrangeCoins(1), 1)
print(Solution().arrangeCoins(2), 1)
print(Solution().arrangeCoins(3), 2)
print(Solution().arrangeCoins(4), 2)
print(Solution().arrangeCoins(5), 2)
print(Solution().arrangeCoins(6), 3)
print(Solution().arrangeCoins(8), 3)