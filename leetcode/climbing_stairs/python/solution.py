class Solution:
    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, pure recursion, tle
        'counter' as a return statement from dfs
        converts to top-down
        """
        def dfs(index: int) -> int:
            if index < 0:
                return 0
            elif index == 0:
                return 1

            return dfs(index - 1) + dfs(index - 2)

        return dfs(number)

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute force, shared state, tle
        `counter` as shared variable (list)
        """
        self.counter = 0

        def dfs(index: int) -> int:
            if index < 0:
                return
            elif index == 0:
                self.counter += 1
                return

            dfs(index - 1)
            dfs(index - 2)

        dfs(number)
        return self.counter

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {0: 1}

        def dfs(index: int) -> int:
            if index < 0:
                return 0
            elif index in memo:
                return memo[index]

            memo[index] = dfs(index - 1) + dfs(index - 2)
            return memo[index]

        return dfs(number)

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        memo = [None] * (number + 1)
        memo[0] = 1

        def dfs(index: int) -> int:
            if index < 0:
                return 0
            elif memo[index] is not None:
                return memo[index]

            memo[index] = dfs(index - 1) + dfs(index - 2)
            return memo[index]

        return dfs(number)

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        if number < 4:
            return number

        cache = [1] * (number + 1)

        for index in range(2, number + 1):
            cache[index] = cache[index - 1] + cache[index - 2]

        return cache[number]

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        if number < 4:
            return number

        cache = [1, 1]

        for index in range(2, number + 1):
            cache = [cache[1], cache[0] + cache[1]]

        return cache[-1]

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: slick
        """
        if number < 4:
            return number

        a = 0
        b = 1

        for index in range(number):
            b = a + b
            a = b - a
            # (a, b) = (b, a + b)

        return b


print(Solution().climbStairs(1) == 1)
print(Solution().climbStairs(2) == 2)
print(Solution().climbStairs(3) == 3)
print(Solution().climbStairs(4) == 5)
print(Solution().climbStairs(5) == 8)
print(Solution().climbStairs(6) == 13)