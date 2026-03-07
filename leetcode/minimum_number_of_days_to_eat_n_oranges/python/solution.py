class Solution:
    def minDays(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = n
        memo = [-1] * (N + 1)
        memo[0] = 0

        def dfs(n):
            if n < 0:
                return N
            elif memo[n] != -1:
                return memo[n]

            # Eat one orange.
            res = 1 + dfs(n - 1)

            # If divisible by 2.
            if (n % 2 == 0):
                res = min(res, 1 + dfs(n // 2))

            # If divisible by 3.
            if (n % 3 == 0):
                res = min(res, 1 + dfs(n // 3))

            memo[n] = res
            return res

        return dfs(n)


class Solution:
    def minDays(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: greedy, top-down
        """
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 1

        def dfs(n):
            if memo[n] != -1:
                return memo[n]

            memo[n] = min(
                dfs(n//2) + 1 + (n % 2),
                dfs(n//3) + 1 + (n % 3)
            )

            return memo[n]

        return dfs(n)


class Solution:
    def minDays(self, n: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags:
            DS: hash map
            A: greedy, top-down
        """
        memo = {0: 0, 1: 1}

        def dfs(n):
            if n in memo:
                return memo[n]

            memo[n] = min(
                dfs(n//2) + 1 + (n % 2),
                dfs(n//3) + 1 + (n % 3)
            )

            return memo[n]

        return dfs(n)


print(Solution().minDays(61455274) == 29)
print(Solution().minDays(10) == 4)
print(Solution().minDays(6) == 3)
print(Solution().minDays(429) == 12)
print(Solution().minDays(820592) == 22)
