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


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = {}  # {(index, buying? (else selling)): profit}

        def dfs(index, buying):
            if index >= len(prices):
                return 0
            elif (index, buying) in memo:
                return memo[(index, buying)]
            elif buying:
                memo[(index, buying)] = max(
                    dfs(index + 1, True),
                    -prices[index] + dfs(index + 1, False)
                )
            else:
                memo[(index, buying)] = max(
                    dfs(index + 1, False),
                    prices[index] + dfs(index + 2, True)
                )
            return memo[(index, buying)]

        return dfs(0, True)


print(Solution().maxProfit([1, 2, 3, 0, 2]) == 3)
print(Solution().maxProfit([1]) == 0)
print(Solution().maxProfit([2, 1, 4]) == 3)