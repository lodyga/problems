class Solution:
    def maxProfit(self, prices):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

    def maxProfit(self, prices):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: two pointers
        """
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:  # if price is lower buy
                left = right
            else:  # if price is higher calculate revenue
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)
print(Solution().maxProfit([2, 4, 1]) == 2)
print(Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2)
print(Solution().maxProfit([1, 2]) == 1)
