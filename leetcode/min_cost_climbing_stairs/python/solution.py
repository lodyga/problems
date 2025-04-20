class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, pure recursion, tle
        converts to top-down
        """
        def dfs(index):
            if index < 0:
                return 0

            return cost[index] + min(dfs(index - 1), dfs(index - 2))

        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, function argument, tle
        """
        self.min_total_cost = sum(cost)

        def dfs(index, total_cost):
            if index < 0:
                self.min_total_cost = min(self.min_total_cost, total_cost)
                return

            dfs(index - 1, total_cost + cost[index])
            dfs(index - 2, total_cost + cost[index])

        dfs(len(cost) - 1, 0)
        dfs(len(cost) - 2, 0)
        return self.min_total_cost

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, backtracking, tle
        """
        self.total_cost = 0
        self.min_total_cost = sum(cost)

        def dfs(index):
            if index < 0:
                self.min_total_cost = min(self.min_total_cost, self.total_cost)
                return

            self.total_cost += cost[index]
            dfs(index - 1)
            dfs(index - 2)
            self.total_cost -= cost[index]

        dfs(len(cost) - 1)
        dfs(len(cost) - 2)
        return self.min_total_cost

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, function argument, tle
        """
        def dfs(index, total_cost):
            if index < 0:
                return total_cost

            return min(
                dfs(index - 1, total_cost + cost[index]),
                dfs(index - 2, total_cost + cost[index]))

        return min(dfs(len(cost) - 1, 0), dfs(len(cost) - 2, 0))

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        memo = [None] * len(cost)
        memo[:2] = cost[:2]

        def dfs(index):
            if memo[index] is not None:
                return memo[index]

            memo[index] = cost[index] + min(dfs(index - 1), dfs(index - 2))
            return memo[index]

        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {0: cost[0], 1: cost[1]}

        def dfs(index):
            if index in memo:
                return memo[index]

            memo[index] = cost[index] + min(dfs(index - 1), dfs(index - 2))
            return memo[index]

        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [None] * len(cost)
        cache[:2] = cost[:2]

        for index in range(2, len(cost)):
            cache[index] = cost[index] + \
                min(cache[index - 1], cache[index - 2])

        return min(cache[-2:])

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        mutate input list
        """
        for index in range(2, len(cost)):
            cost[index] += min(cost[index - 1], cost[index - 2])

        return min(cost[-2:])

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = cost[:2]

        for index in range(2, len(cost)):
            cache = [cache[1], cost[index] + min(cache[0], cache[1])]

        return min(cache)

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        a = cost[0]
        b = cost[1]

        for index in range(2, len(cost)):
            a, b = b, cost[index] + min(a, b)

        return min(a, b)


print(Solution().minCostClimbingStairs([10, 15, 20]) == 15)
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6)
