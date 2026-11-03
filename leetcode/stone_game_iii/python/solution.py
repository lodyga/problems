class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        def dfs(start: int):
            if start == N:
                return 0
            elif memo[start] != INT_MIN:
                return memo[start]

            score = INT_MIN
            end = min(start + 3, N)
            subpile_sum = 0

            for idx in range(start, end):
                subpile_sum += stones[idx]
                score = max(score, subpile_sum - dfs(idx + 1))

            memo[start] = score
            return score

        INT_MIN = -10**8
        N = len(stones)
        memo = [INT_MIN] * N
        res = dfs(0)

        if res > 0:
            return "Alice"
        elif res == 0:
            return "Tie"
        else:
            return "Bob"


class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: bottem-up
        """
        INT_MIN = -10**8
        N = len(stones)
        cache = [0] * (N + 1)

        for idx in range(N - 1, -1, -1):
            cache[idx] = INT_MIN
            end = min(idx + 3, N)
            subpile_sum = 0

            for jdx in range(idx, end):
                subpile_sum += stones[jdx]
                cache[idx] = max(
                    cache[idx],
                    subpile_sum - cache[jdx + 1]
                )

        if cache[0] > 0:
            return "Alice"
        elif cache[0] == 0:
            return "Tie"
        else:
            return "Bob"


print(Solution().stoneGameIII([1, 2, 3, 7]) == "Bob")
print(Solution().stoneGameIII([1, 2, 3, -9]) == "Alice")
print(Solution().stoneGameIII([1, 2, 3, 6]) == "Tie")
print(Solution().stoneGameIII([-1, -2]) == "Alice")
print(Solution().stoneGameIII([-1, -2, -3]) == "Tie")
print(Solution().stoneGameIII([-13, 17, 7, -13, 6, -3, -15, 15, -3, 4, 6, -5, 16, 0, 12, -6, 8, 13, 15, -4, -11, -16, 15]) == "Alice")
