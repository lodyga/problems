class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index, alice_to_move):
            if index >= len(stones):
                return 0

            score = -10**9
            substone_sum = 0
            for x in range(index, min(index + 3, len(stones))):
                substone_sum += stones[x]
                points = substone_sum - dfs(x + 1, not alice_to_move)
                score = max(score, points)
            return score

        res = dfs(0, True)
        return "Tie" if res == 0 else "Alice" if res > 0 else "Bob"


class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}

        def dfs(index, alice_to_move):
            if index >= len(stones):
                return 0
            elif (index, alice_to_move) in memo:
                return memo[(index, alice_to_move)]

            score = -10**9
            substone_sum = 0
            for x in range(index, min(index + 3, len(stones))):
                substone_sum += stones[x]
                points = substone_sum - dfs(x + 1, not alice_to_move)
                score = max(score, points)

            memo[(index, alice_to_move)] = score
            return score

        return "Tie" if dfs(0, True) == 0 else "Alice" if dfs(0, True) > 0 else "Bob"


print(Solution().stoneGameIII([1, 2, 3, 7]), "Bob")
print(Solution().stoneGameIII([1, 2, 3, -9]), "Alice")
print(Solution().stoneGameIII([1, 2, 3, 6]), "Tie")
print(Solution().stoneGameIII([-1, -2]), "Alice")
print(Solution().stoneGameIII([-1, -2, -3]), "Tie")
print(Solution().stoneGameIII([-13, 17, 7, -13, 6, -3, -15, 15, -3, 4, 6, -5, 16, 0, 12, -6, 8, 13, 15, -4, -11, -16, 15]), "Alice")