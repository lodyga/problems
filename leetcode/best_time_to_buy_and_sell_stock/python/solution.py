class Solution:
    def maxProfit(self, prices):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        min_price = prices[0]
        res = 0

        for price in prices:
            if price > min_price:
                res = max(res, price - min_price)
            else:
                min_price = price

        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)
print(Solution().maxProfit([2, 4, 1]) == 2)
print(Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2)
print(Solution().maxProfit([1, 2]) == 1)
