class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [[-1] * 2 for _ in range(len(prices) + 2)]
        memo[-1] = memo[-2] = [0, 0]

        def dfs(index: int, can_buy: bool) -> int:
            if memo[index][can_buy] != -1:
                return memo[index][can_buy]

            price = prices[index]
            buy = sell = 0
            skip = dfs(index + 1, can_buy)
            if can_buy:
                buy = -price + dfs(index + 1, False)
            else:
                sell = price + dfs(index + 2, True)
            res = max(skip, buy, sell)
            memo[index][can_buy] = res
            return res

        return dfs(0, True)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [[0] * 2 for _ in range(len(prices) + 2)]
        cache[-1] = cache[-2] = [0, 0]

        for index in range(len(prices) - 1, -1, -1):
            price = prices[index]
            # can buy
            cache[index][1] = max(
                cache[index + 1][1], # skip
                -price + cache[index + 1][0] # buy
            )
            # can sell
            cache[index][0] = max(
                cache[index + 1][0], # skip
                price + cache[index + 2][1] # sell
            )

        return cache[0][1]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [[0, 0], [0, 0]]

        for index in range(len(prices) - 1, -1, -1):
            price = prices[index]
            # can buy
            buy_cache = max(
                cache[0][1], # skip
                -price + cache[0][0] # buy
            )
            # can sell
            sell_cache = max(
                cache[0][0], # skip
                price + cache[1][1] # sell
            )
            cache[1][0] = cache[0][0]
            cache[1][1] = cache[0][1]
            cache[0][0] = sell_cache
            cache[0][1] = buy_cache

        return cache[0][1]


print(Solution().maxProfit([1, 2, 3, 0, 2]) == 3)
print(Solution().maxProfit([1]) == 0)
print(Solution().maxProfit([2, 1, 4]) == 3)
