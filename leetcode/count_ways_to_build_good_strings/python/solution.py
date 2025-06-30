r"""
draft
[1, 1, 1, 1]
"0", "1"

[1, 2, 1, 1]
"0", "1", "00", "01", "10", "11"

[2, 2, 1, 1]
"00", "01", "10", "11"
2**2 = 4

[3, 3, 1, 1]
2**3 + 2**2 + 2**1 = 8 + 4 + 2 = 14

[2, 3, 1, 2]
"00", "11", "000", "110", and "011"
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        mod = 10**9 + 7

        def dfs(index: int) -> int:
            if index > high:
                return 0
            
            memo = 1 if index >= low else 0
            memo += dfs(index + zero)
            memo += dfs(index + one)

            return memo % mod

        return dfs(0)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        mod = 10**9 + 7
        # represents the total number of valid good strings that can be constructed starting from length index and going up to high
        memo = {}  # {string_length: good string counter}

        def dfs(index: int) -> int:
            if index > high:
                return 0
            elif index in memo:
                return memo[index]
            
            memo[index] = 1 if index >= low else 0
            memo[index] += dfs(index + zero)
            memo[index] += dfs(index + one)

            return memo[index] % mod

        return dfs(0)


print(Solution().countGoodStrings(1, 1, 1, 1) == 2)
print(Solution().countGoodStrings(2, 2, 1, 1) == 4)
print(Solution().countGoodStrings(1, 2, 1, 1) == 6)
print(Solution().countGoodStrings(1, 3, 1, 1) == 14)
print(Solution().countGoodStrings(3, 3, 1, 1) == 8)
print(Solution().countGoodStrings(2, 3, 1, 2) == 5)
print(Solution().countGoodStrings(200, 200, 10, 1) == 764262396)
print(Solution().countGoodStrings(1, 100000, 1, 1) == 215447031)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        O(n), O(n)
        dp, bottom-up
        """
        mod = 10**9 + 7
        cache = {}  # memo[string length]: store the number of ways to make a good string of length index
        cache[0] = 1  # one way to create zero length (empty) string

        for index in range(1, high + 1):
            cache[index] = (
                cache.get(index - zero, 0) + 
                cache.get(index - one, 0)
            ) % mod
        
        return sum(cache[index]
                   for index in range(low, high + 1)
                   ) % mod