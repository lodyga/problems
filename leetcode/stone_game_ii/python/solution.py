class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        UPPER_BOUND = 10**6

        def dfs(start: int, m: int, is_alice_turn: bool) -> int:
            if start == len(piles):
                return 0

            score = 0 if is_alice_turn else UPPER_BOUND
            subpile_sum = 0

            for index in range(start, min(start + 2*m, len(piles))):
                subpile_sum += piles[index]

                get_rest_piles = dfs(
                    index + 1,
                    max(m, index - start + 1),
                    not is_alice_turn
                )

                if is_alice_turn:
                    score = max(score, subpile_sum + get_rest_piles)
                else:
                    score = min(score, get_rest_piles)

            return score

        return dfs(0, 1, True)


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: hash map
            A: top-down, prefix sum
        """
        UPPER_BOUND = 10**6
        memo = {}
        prefix = [0]
        for pile in piles:
            prefix.append(prefix[-1] + pile)

        def dfs(start: int, m: int, is_alice_turn: bool) -> int:
            memo_ind = (start, m, is_alice_turn)

            if start == len(piles):
                return 0
            elif memo_ind in memo:
                return memo[memo_ind]

            score = 0 if is_alice_turn else UPPER_BOUND

            for index in range(start, min(start + 2*m, len(piles))):
                subpile_sum = prefix[index + 1] - prefix[start]

                get_rest_piles = dfs(
                    index + 1,
                    max(m, index - start + 1),
                    not is_alice_turn
                )

                if is_alice_turn:
                    score = max(score, subpile_sum + get_rest_piles)
                else:
                    score = min(score, get_rest_piles)

            memo[memo_ind] = score
            return score

        return dfs(0, 1, True)


print(Solution().stoneGameII([2, 7]) == 9)
print(Solution().stoneGameII([2, 7, 9, 4, 4]) == 10)
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]) == 104)
print(Solution().stoneGameII([2, 100]) == 102)
print(Solution().stoneGameII([1, 2, 100]) == 3)
print(Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]) == 217)
print(Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]) == 98008)
