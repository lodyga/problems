class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        # the total number of valid good strings that can be constructed starting from length index and going up to high
        memo = [-1] * (high + max(zero, one))

        def dfs(idx: int) -> int:
            if idx > high:
                return 0
            elif memo[idx] != -1:
                return memo[idx]

            res = 1 if low <= idx <= high else 0

            res += dfs(idx + zero)
            res += dfs(idx + one)

            memo[idx] = res % MOD
            return memo[idx]

        dfs(0)
        return memo[0]


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
        cache[high] = 1

        for idx in range(high - 1, -1, -1):
            if idx + zero <= high:
                cache[idx] += cache[idx + zero]
            
            if idx + one <= high:
                cache[idx] += cache[idx + one]
            
            cache[idx] %= MOD

        return sum(cache[idx] 
                   for idx in range(high - low + 1)) % MOD


print(Solution().countGoodStrings(3, 3, 1, 1) == 8)
print(Solution().countGoodStrings(2, 3, 1, 2) == 5)
print(Solution().countGoodStrings(1, 1, 1, 1) == 2)
print(Solution().countGoodStrings(2, 2, 1, 1) == 4)
print(Solution().countGoodStrings(1, 2, 1, 1) == 6)
print(Solution().countGoodStrings(1, 3, 1, 1) == 14)
print(Solution().countGoodStrings(200, 200, 10, 1) == 764262396)
print(Solution().countGoodStrings(1, 100000, 1, 1) == 215447031)
