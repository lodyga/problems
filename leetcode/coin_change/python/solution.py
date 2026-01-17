from collections import deque


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(2^n)
            O(coins^amount)
        Auxiliary space complexity: O(n)
            O(amount)
        Tags: brute-force
        """
        coins.sort(reverse=True)

        def dfs(total: int) -> int:
            if total == amount:
                return 0
            elif total > amount:
                return amount + 1

            coin_counter = amount + 1
            for coin in coins:
                coin_counter = min(coin_counter, 1 + dfs(total + coin))

            return coin_counter

        res = dfs(0)
        return res if res != amount + 1 else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
            O(c*a)
            c: coin denominations
            a: ammonut size
        Auxiliary space complexity: O(n)
            O(amount)
        Tags:
            DS: hash map
            A: top-down
        """
        coins.sort(reverse=True)
        # {amount: min coins to get target amount}
        memo = {amount: 0}

        def dfs(total: int) -> int:
            if total > amount:
                return amount + 1
            elif total in memo:
                return memo[total]

            coin_counter = amount + 1
            for coin in coins:
                coin_counter = min(coin_counter, 1 + dfs(total + coin))

            memo[total] = coin_counter
            return coin_counter

        res = dfs(0)
        return res if res != amount + 1 else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
            O(c*a)
            c: coin denominations
            a: ammonut size
        Auxiliary space complexity: O(n)
            O(amount)
        Tags:
            DS: array
            A: top-down
        """
        coins.sort(reverse=True)
        # [amount left: min coins to get target amount left]
        memo = [-1] * (amount + 1)
        memo[-1] = 0

        def dfs(total: int) -> int:
            if total > amount:
                return amount + 1
            elif memo[total] != -1:
                return memo[total]

            coin_counter = amount + 1
            for coin in coins:
                coin_counter = min(coin_counter, 1 + dfs(total + coin))

            memo[total] = coin_counter
            return coin_counter

        res = dfs(0)
        return res if res != amount + 1 else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
            O(c*a)
            c: coin denominations
            a: ammonut size
        Auxiliary space complexity: O(n)
            O(amount)
        Tags:
            DS: hash map
            A: bottom-up
        """
        # Min number of coins needed to get target amount (equal to the index).
        # No coins needed to get to 0 amount.
        cache = {0: 0}

        for index in range(1, amount + 1):
            for coin in coins:
                if coin > index:
                    continue
                cache[index] = min(
                    cache.get(index, amount + 1),
                    1 + cache.get(index - coin, amount + 1)
                )

        res = cache.get(amount, amount + 1)
        return res if res != amount + 1 else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
            O(c*a)
            c: coin denominations
            a: ammonut size
        Auxiliary space complexity: O(n)
            O(amount)
        Tags:
            DS: array
            A: bottom-up
        """
        # Min number of coins needed to get target amount (equal to the index).
        cache = [amount + 1] * (amount + 1)
        # No coins needed to get to 0 amount amount.
        cache[0] = 0

        for index in range(1, amount + 1):
            for coin in coins:
                if coin > index:
                    continue
                cache[index] = min(cache[index], 1 + cache[index - coin])

        res = cache[amount]
        return res if res != amount + 1 else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time complexity: O(n2)
            O(c*a)
            c: coin denominations
            a: ammonut size
        Auxiliary space complexity: O(n)
            O(amount)
        Tags:
            DS: queue
            A: bfs, iteration, queue
        """
        if amount == 0:
            return 0

        def bfs(node):
            queue = deque([node])
            level = 0
            visited = [False] * (amount + 1)
            visited[0] = True

            while queue:
                level += 1
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for coin in coins:
                        total = node + coin

                        if total == amount:
                            return level
                        elif total > amount:
                            continue
                        elif visited[total]:
                            continue

                        queue.append(total)
                        visited[total] = True
            return -1

        return bfs(0)


print(Solution().coinChange([5], 5) == 1)
print(Solution().coinChange([1, 2], 3) == 2)
print(Solution().coinChange([1, 2, 5], 11) == 3)
print(Solution().coinChange([2], 3) == -1)
print(Solution().coinChange([2], 1) == -1)
print(Solution().coinChange([1], 0) == 0)
print(Solution().coinChange([2, 5, 10, 1], 27) == 4)
print(Solution().coinChange([186, 419, 83, 408], 6249) == 20)
