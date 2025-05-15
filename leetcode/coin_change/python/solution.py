class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as list
        """
        # min number of coins needed to get target amount (equal to the index)
        # "anmount + 1" an imposbile value stays when the last element of min_coins was not modified
        cache = [amount + 1] * (amount + 1)
        # no coins needed to get 0
        cache[0] = 0

        for index in range(1, amount + 1):
            for coin in coins:
                if index >= coin:
                    cache[index] = min(cache[index],
                                       cache[index - coin] + 1)

        return (cache[amount]
                if cache[amount] != amount + 1
                else -1)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as hash map
        """
        # min number of coins needed to get target amount (equal to the index)
        cache = {0: 0}

        for index in range(1, amount + 1):
            for coin in coins:
                if index >= coin:
                    cache[index] = min(cache.get(index, amount + 1),
                                       cache.get(index - coin, amount + 1) + 1)

        return (cache.get(amount, -1)
                if cache.get(amount, -1) != amount + 1
                else -1)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        # [min coins to get index amount]
        memo = [None] * (amount + 1)
        memo[0] = 0
        base_amount = amount

        def dfs(amount):
            if amount < 0:
                return base_amount + 1
            elif memo[amount] is not None:
                return memo[amount]

            memo[amount] = min(1 + dfs(amount - coin)
                               for coin in coins)

            return memo[amount]

        coin_count = dfs(amount)
        return (coin_count
                if coin_count <= amount
                else -1)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        base_amount = amount
        memo = {0: 0}  # {ammont: min coins to get that amount}

        def dfs(amount):
            if amount < 0:
                return base_amount + 1  # return impossible value
            elif amount in memo:
                return memo[amount]

            memo[amount] = min(1 + dfs(amount - coin)
                               for coin in coins)

            return memo[amount]

        coin_count = dfs(amount)
        return (coin_count
                if coin_count <= amount
                else -1)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(2^n)
            O(coins^amount)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        base_amount = amount

        def dfs(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return base_amount + 1

            return min(1 + dfs(amount - coin)
                       for coin in coins)

        coin_count = dfs(amount)
        return (coin_count
                if coin_count <= amount
                else -1)


print(Solution().coinChange([5], 5) == 1)
print(Solution().coinChange([1, 2], 3) == 2)
print(Solution().coinChange([1, 2, 5], 11) == 3)
print(Solution().coinChange([2], 3) == -1)
print(Solution().coinChange([2], 1) == -1)
print(Solution().coinChange([1], 0) == 0)
print(Solution().coinChange([2, 5, 10, 1], 27) == 4)
print(Solution().coinChange([186, 419, 83, 408], 6249) == 20)