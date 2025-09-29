class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        if len(prices) == 1:
            return 0
        
        prev_price = prices[0]
        profit = 0
        
        for price in prices[1:]:
            if prev_price < price:
                profit += (price - prev_price)
            prev_price = price

        return profit


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoziation as hash map
        """
        memo = {}  # {(index, can buy): profit, }

        def dfs(index, can_buy):
            if index == len(prices):
                return 0
            elif (index, can_buy) in memo:
                return memo[(index, can_buy)]
            
            if can_buy:
                profit = max(
                    -prices[index] + dfs(index + 1, False),  # buy
                    dfs(index + 1, True)  # wait
                )
            else:
                profit = max(
                    prices[index] + dfs(index + 1, True),  # sell
                    dfs(index + 1, False)  # wait
                )

            memo[(index, can_buy)] = profit
            return profit
        
        return dfs(0, True)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoziation as hash map
        """
        memo = {}  # {(index, can buy): profit, }

        def dfs(index, can_buy):
            if index == len(prices):
                return 0
            elif (index, can_buy) in memo:
                return memo[(index, can_buy)]
            
            buy_or_sell = prices[index] * (-1 if can_buy else 1) + dfs(index + 1, not can_buy)
            wait = dfs(index + 1, can_buy)
            memo[(index, can_buy)] = max(buy_or_sell, wait)
            return memo[(index, can_buy)]

        return dfs(0, True)


print(Solution().maxProfit([7, 1]) == 0)
print(Solution().maxProfit([1, 7]) == 6)
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7)
print(Solution().maxProfit([1, 2, 3, 4, 5]) == 4)
print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)