class Solution:
    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: brute-force, pure recursion
        'counter' as a return statement from dfs
        converts to top-down
        """
        def dfs(index: int) -> int:
            if index in (0, 1):
                return 1
            return dfs(index - 1) + dfs(index - 2)
        return dfs(steps)

    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: brute-force, shared state
        `counter` as shared variable
        """
        counter = 0

        def dfs(index: int) -> int:
            nonlocal counter
            if index in (0, 1):
                counter += 1
                return
            dfs(index - 1)
            dfs(index - 2)
        dfs(steps)
        return counter

    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash map
            A: top-down
        """
        memo = {0: 1, 1: 1}

        def dfs(index: int) -> int:
            if index in memo:
                return memo[index]
            memo[index] = dfs(index - 1) + dfs(index - 2)
            return memo[index]
        return dfs(steps)

    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        memo = [-1] * (steps + 1)
        memo[0] = 1
        memo[1] = 1

        def dfs(index: int) -> int:
            if memo[index] != -1:
                return memo[index]
            memo[index] = dfs(index - 1) + dfs(index - 2)
            return memo[index]
        return dfs(steps)

    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: bottom-up
        """
        cache = [1] * (steps + 1)
        for index in range(2, steps + 1):
            cache[index] = cache[index - 1] + cache[index - 2]
        return cache[steps]

    def climbStairs(self, steps: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: bottom-up
        """
        index = 1
        cache = [1, 1]
        for index in range(2, steps + 1):
            cache[index % 2] = cache[0] + cache[1]
        return cache[steps % 2]

    def climbStairs(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bottom-up
        """
        a = 0
        b = 1
        for _ in range(number):
            (a, b) = (b, a + b)
            # b = a + b
            # a = b - a
        return b


print(Solution().climbStairs(1) == 1)
print(Solution().climbStairs(2) == 2)
print(Solution().climbStairs(3) == 3)
print(Solution().climbStairs(4) == 5)
print(Solution().climbStairs(5) == 8)
print(Solution().climbStairs(6) == 13)
print(Solution().climbStairs(44) == 1134903170)
