class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        MOD = 10**9 + 7
        # the total number of valid good strings that can be constructed starting from length index and going up to high
        memo = [-1] * (high + max(zero, one))

        def dfs(index: int) -> int:
            # index: current string length
            if index > high:
                return 0
            elif memo[index] != -1:
                return memo[index]

            res = 1 if index >= low else 0
            res += dfs(index + zero)
            res += dfs(index + one)
            memo[index] = res
            return res % MOD

        return dfs(0)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: bottom-up
        """
        MOD = 10**9 + 7
        # the total number of strings that can be constructed starting from length index and going up to high
        cache = [0] * (high + 1)
        cache[0] = 1

        for index in range(1, high + 1):
            if index >= zero:
                cache[index] += cache[index - zero]
            if index >= one:
                cache[index] += cache[index - one]
            cache[index] %= MOD

        return sum(cache[index] for index in range(low, high + 1)) % MOD


print(Solution().countGoodStrings(1, 1, 1, 1) == 2)
print(Solution().countGoodStrings(2, 2, 1, 1) == 4)
print(Solution().countGoodStrings(1, 2, 1, 1) == 6)
print(Solution().countGoodStrings(1, 3, 1, 1) == 14)
print(Solution().countGoodStrings(3, 3, 1, 1) == 8)
print(Solution().countGoodStrings(2, 3, 1, 2) == 5)
print(Solution().countGoodStrings(200, 200, 10, 1) == 764262396)
print(Solution().countGoodStrings(1, 100000, 1, 1) == 215447031)
