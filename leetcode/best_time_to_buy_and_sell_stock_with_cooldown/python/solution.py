class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = {}  # {(index, can_buy? (else selling)): profit}

        def dfs(index, can_buy):
            if index >= len(prices):
                return 0
            elif (index, can_buy) in memo:
                return memo[(index, can_buy)]
            elif can_buy:
                buy = -prices[index] + dfs(index + 1, False)
                wait = dfs(index + 1, can_buy)
                memo[(index, can_buy)] = max(buy, wait)
            else:
                sell = prices[index] + dfs(index + 2, True)
                wait = dfs(index + 1, can_buy)
                memo[(index, can_buy)] = max(sell, wait)

            return memo[(index, can_buy)]
        
        return dfs(0, True)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = {}  # {(index, can_buy? (else selling)): profit}

        def dfs(index, can_buy):
            if index >= len(prices):
                return 0
            elif (index, can_buy) in memo:
                return memo[(index, can_buy)]
            
            no_wait = (
                # buy or sell
                + prices[index] * (-1 if can_buy else 1)
                + dfs(index + (1 if can_buy else 2), not can_buy)
            )
            wait = dfs(index + 1, can_buy)
            memo[(index, can_buy)] = max(no_wait, wait)
            return memo[(index, can_buy)]
        
        return dfs(0, True)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = [None] * len(prices)

        def dfs(index):
            if index >= len(prices):
                return 0
            elif memo[index] is not None:
                return memo[index]

            memo[index] = dfs(index + 1)
            for index2 in range(index + 1, len(prices)):
                memo[index] = max(
                    memo[index],
                    prices[index2] - prices[index] + dfs(index2 + 2)
                )
            return memo[index]

        return dfs(0)


print(Solution().maxProfit([1, 2, 3, 0, 2]) == 3)
print(Solution().maxProfit([1]) == 0)
print(Solution().maxProfit([2, 1, 4]) == 3)