class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoziation as hash map
        """
        memo = {}

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


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7)
print(Solution().maxProfit([1, 2, 3, 4, 5]) == 4)
print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)