class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        # coins.sort(reverse=True)
        memo = {}

        def dfs(index, remaining):
            if remaining == 0:
                return 1
            elif (
                index >= len(coins) or
                remaining < 0
            ):
                return 0
            elif (index, remaining) in memo:
                return memo[(index, remaining)]
            
            taken = dfs(index, remaining - coins[index])
            skipped = dfs(index + 1, remaining)
            memo[(index, remaining)] = skipped + taken
            return memo[(index, remaining)]

        return dfs(0, amount)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        # coins.sort(reverse=True)
        memo = {}

        def dfs(index, remaining):
            if remaining == 0:
                return 1
            elif (
                index >= len(coins) or
                remaining < 0
            ):
                return 0
            elif (index, remaining) in memo:
                return memo[(index, remaining)]

            memo[(index, remaining)] = 0
            for i in range(index, len(coins)):
                memo[(index, remaining)] += dfs(i, remaining - coins[i])

            # taken = dfs(index, remaining - coins[index])
            # skipped = dfs(index + 1, remaining)
            # memo[(index, remaining)] = taken + skipped
            return memo[(index, remaining)]

        return dfs(0, amount)


print(Solution().change(10, [10]), 1)
print(Solution().change(3, [2]), 0)
print(Solution().change(5, [1, 2, 5]), 4)
print(Solution().change(500, [3, 5, 7, 8, 9, 10, 11]), 35502874)