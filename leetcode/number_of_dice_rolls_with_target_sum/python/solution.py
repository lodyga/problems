class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            k: die side count
            t: target
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags:
            DS: hash map
            A: top-down
        """
        MOD = 10**9 + 7
        memo = {}

        def dfs(index: int, total: int) -> int:
            if index == n:
                return 1 if total == target else 0
            elif total > target:
                return 0
            elif (index, total) in memo:
                return memo[index, total]

            res = 0

            for side in range(1, k + 1):
                res += dfs(index + 1, total + side)

            res %= MOD
            memo[index, total] = res
            return res

        return dfs(0, 0)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            k: die side count
            t: target
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags:
            DS: array
            A: top-down
        """
        MOD = 10**9 + 7
        memo = [[-1] * (target + 1) for _ in range(n)]

        def dfs(index: int, total: int) -> int:
            if index == n:
                return 1 if total == target else 0
            elif total > target:
                return 0
            elif memo[index][total] != -1:
                return memo[index][total]

            res = 0

            for side in range(1, k + 1):
                res += dfs(index + 1, total + side)

            res %= MOD
            memo[index][total] = res
            return res

        return dfs(0, 0)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            k: die side count
            t: target
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags:
            DS: array
            A: bottom-up
        """
        MOD = 10**9 + 7
        cache = [[0] * (target + 1) for _ in range(n + 1)]
        cache[-1][-1] = 1

        for index in range(n - 1, -1, -1):
            for side in range(1, k + 1):
                for total in range(target + 1 - side):
                    cache[index][total] += cache[index + 1][total + side]
                    cache[index][total] %= MOD

        return cache[0][0]


print(Solution().numRollsToTarget(1, 6, 3) == 1)
print(Solution().numRollsToTarget(2, 6, 7) == 6)
print(Solution().numRollsToTarget(3, 6, 9) == 25)
print(Solution().numRollsToTarget(30, 30, 500) == 222616187)
