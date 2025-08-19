class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index, alice_to_move):
            if index == len(stoneValue):
                return 0
            
            part_sum = 0
            result = float("-inf")
            for x in range(index, min(index + 3, len(stoneValue))):
                part_sum += stoneValue[x]
                score = part_sum - dfs(x + 1, not alice_to_move)
                result = max(result, score)
            return result

        result = dfs(0, True)
        return "Tie" if result == 0 else "Alice" if result > 0 else "Bob"


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {index: winner}

        def dfs(index, alice_to_move):
            if index == len(stoneValue):
                return 0
            elif index in memo:
                return memo[index]
            
            part_sum = 0
            memo[index] = float("-inf")
            for x in range(index, min(index + 3, len(stoneValue))):
                part_sum += stoneValue[x]
                score = part_sum - dfs(x + 1, not alice_to_move)
                memo[index] = max(memo[index], score)
            return memo[index]

        result = dfs(0, True)
        return "Tie" if result == 0 else "Alice" if result > 0 else "Bob"


print(Solution().stoneGameIII([1, 2, 3, 7]), "Bob")
print(Solution().stoneGameIII([1, 2, 3, -9]), "Alice")
print(Solution().stoneGameIII([1, 2, 3, 6]), "Tie")
print(Solution().stoneGameIII([-1, -2]), "Alice")
print(Solution().stoneGameIII([-1, -2, -3]), "Tie")