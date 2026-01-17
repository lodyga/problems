class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        UPPER_BOUND = 10**8
        LOWER_BOUND = -UPPER_BOUND
        memo_alice = {}
        
        def dfs_alice(start: int, is_alice_turn: bool) -> int:
            memo_index = (start, is_alice_turn)
            
            if start == len(stones):
                return 0
            elif memo_index in memo_alice:
                return memo_alice[memo_index]

            subpile_sum = 0
            score = LOWER_BOUND if is_alice_turn else UPPER_BOUND

            for index in range(start, min(start + 3, len(stones))):
                subpile_sum += stones[index]
                get_rest_piles = dfs_alice(index + 1, not is_alice_turn)

                if is_alice_turn:
                    score = max(score, subpile_sum + get_rest_piles)
                else:
                    score = min(score, get_rest_piles)

            memo_alice[memo_index] = score
            return score

        memo_bob = {}
        def dfs_bob(start: int, is_alice_turn: bool) -> int:
            memo_index = (start, is_alice_turn)
            
            if start == len(stones):
                return 0
            elif memo_index in memo_bob:
                return memo_bob[memo_index]

            subpile_sum = 0
            score = LOWER_BOUND if not is_alice_turn else UPPER_BOUND

            for index in range(start, min(start + 3, len(stones))):
                subpile_sum += stones[index]
                get_rest_piles = dfs_bob(index + 1, not is_alice_turn)

                if is_alice_turn:
                    score = min(score, get_rest_piles)
                else:
                    score = max(score, subpile_sum + get_rest_piles)

            memo_bob[memo_index] = score
            return score

        # Maximum stones for Alice - maximum stones for Bob.
        res = dfs_alice(0, True)
        del memo_alice
        res -= dfs_bob(0, True)
        
        return "Tie" if res == 0 else ("Alice" if res > 0 else "Bob")


class Solution:
    def stoneGameIII(self, stones: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        LOWER_BOUND = -10**8
        memo = [-1] * (len(stones) + 1)
        memo[-1] = 0

        def dfs(start):
            if memo[start] != -1:
                return memo[start]

            score = LOWER_BOUND
            subpile_sum = 0
            
            for index in range(start, min(start + 3, len(stones))):
                subpile_sum += stones[index]
                points = subpile_sum - dfs(index + 1)
                score = max(score, points)

            memo[start] = score
            return score

        return "Tie" if dfs(0) == 0 else ("Alice" if dfs(0) > 0 else "Bob")


print(Solution().stoneGameIII([1, 2, 3, 7]) == "Bob")
print(Solution().stoneGameIII([1, 2, 3, -9]) == "Alice")
print(Solution().stoneGameIII([1, 2, 3, 6]) == "Tie")
print(Solution().stoneGameIII([-1, -2]) == "Alice")
print(Solution().stoneGameIII([-1, -2, -3]) == "Tie")
print(Solution().stoneGameIII([-13, 17, 7, -13, 6, -3, -15, 15, -3, 4, 6, -5, 16, 0, 12, -6, 8, 13, 15, -4, -11, -16, 15]) == "Alice")
