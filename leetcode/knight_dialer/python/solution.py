class Solution:
    def knightDialer(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        # index      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # L1:        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        # L2:        [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
        # L3:        [6, 4, 4, 5, 6, 0, 6, 5, 4, 5]

        MOD = 10**9 + 7
        prev_cache = [1] * 10

        for _ in range(1, n):
            cache = [0] * 10
            cache[0] = (prev_cache[4] + prev_cache[6]) % MOD

            # corner
            cache[1] = (prev_cache[6] + prev_cache[8]) % MOD
            cache[3] = (prev_cache[4] + prev_cache[8]) % MOD
            cache[7] = (prev_cache[2] + prev_cache[6]) % MOD
            cache[9] = (prev_cache[2] + prev_cache[4]) % MOD

            # edge
            cache[2] = (prev_cache[7] + prev_cache[9]) % MOD
            cache[8] = (prev_cache[1] + prev_cache[3]) % MOD

            # edge with 0
            cache[4] = (prev_cache[3] + prev_cache[9] + prev_cache[0]) % MOD
            cache[6] = (prev_cache[1] + prev_cache[7] + prev_cache[0]) % MOD

            prev_cache = cache

        return sum(prev_cache) % MOD


print(Solution().knightDialer(1) == 10)
print(Solution().knightDialer(2) == 20)
print(Solution().knightDialer(3) == 46)
print(Solution().knightDialer(3131) == 136006598)
