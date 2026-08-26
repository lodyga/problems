class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = len(prices)
        memo = [[-1, -1] for _ in range(N + 2)]
        memo[-1] = memo[-2] = [0, 0]

        def dfs(idx: int, can_buy: bool) -> int:
            if memo[idx][can_buy] != -1:
                return memo[idx][can_buy]

            price = prices[idx]
            skip = dfs(idx + 1, can_buy)
            buy = sell = 0

            if can_buy:
                buy = -price + dfs(idx + 1, False)
            else:
                sell = price + dfs(idx + 2, True)

            res = max(skip, buy, sell)
            memo[idx][can_buy] = res
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
        N = len(prices)
        cache = [[0, 0] for _ in range(N + 2)]
        cache[-1] = cache[-2] = [0, 0]

        for idx in range(N - 1, -1, -1):
            price = prices[idx]
            cache[idx][True] = max(  # can buy
                cache[idx + 1][True],  # skip
                -price + cache[idx + 1][False]  # buy
            )
            cache[idx][False] = max(  # can sell
                cache[idx + 1][False],  # skip
                price + cache[idx + 2][True]  # sell
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
        N = len(prices)
        cache = [[0, 0], [0, 0]]

        for idx in range(N - 1, -1, -1):
            price = prices[idx]
            buy_cache = max(  # can buy
                cache[0][True],  # skip
                -price + cache[0][False]  # buy
            )
            sell_cache = max(  # can sell
                cache[0][False],  # skip
                price + cache[1][True]  # sell
            )
            cache[1][False] = cache[0][False]
            cache[1][True] = cache[0][True]
            cache[0][False] = sell_cache
            cache[0][True] = buy_cache

        return cache[0][True]


print(Solution().maxProfit([1, 2, 3, 0, 2]) == 3)
print(Solution().maxProfit([1]) == 0)
print(Solution().maxProfit([2, 1, 4]) == 3)
print(Solution().maxProfit([48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11, 94]) == 428)
