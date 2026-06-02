class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(idx: int) -> int:
            if idx == 0:
                return 0
            elif idx == 1:
                return 1
            elif idx == 2:
                return 1

            return (
                dfs(idx - 1)
                + dfs(idx - 2)
                + dfs(idx - 3)
            )

        return dfs(num)


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: top-down
        """
        memo = [-1] * (max(num + 1, 3))
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = (
                dfs(idx - 1)
                + dfs(idx - 2)
                + dfs(idx - 3)
            )

            return memo[idx]

        return dfs(num)


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        memo = {0: 0, 1: 1, 2: 1}

        def dfs(idx: int) -> int:
            if idx in memo:
                return memo[idx]

            memo[idx] = (
                dfs(idx - 1)
                + dfs(idx - 2)
                + dfs(idx - 3)
            )

            return memo[idx]

        return dfs(num)


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bottom-up
        """
        cache = [0, 1, 1]

        for _ in range(3, num + 1):
            cache.append(
                cache[-1]
                + cache[-2]
                + cache[-3]
            )

        return cache[num]


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bottom-up
        """
        cache = [0, 1, 1]

        for idx in range(3, num + 1):
            cache_total = (
                cache[0]
                + cache[1]
                + cache[2]
            )

            cache[idx % 3] = cache_total

        return cache[num % 3]


print(Solution().tribonacci(4) == 4)
print(Solution().tribonacci(25) == 1389537)
print(Solution().tribonacci(0) == 0)
print(Solution().tribonacci(3) == 2)
print(Solution().tribonacci(31) == 53798080)
print(Solution().tribonacci(35) == 615693474)
