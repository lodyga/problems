class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: hash map
            A: top-down
        """
        def dfs(start: int, m: int, is_alice: bool) -> int:
            key = (start, m, is_alice)

            if start == N:
                return 0
            elif key in memo:
                return memo[key]

            score = 0 if is_alice else UPPER_BOUND
            subpile_sum = 0

            for idx in range(start, min(start + 2*m, N)):
                subpile_sum += piles[idx]
                next_dfs = dfs(idx + 1, max(m, idx - start + 1), not is_alice)

                if is_alice:
                    # Alice wants to maximize her final score.
                    score = max(score, subpile_sum + next_dfs)
                else:
                    # Bob wants to minimize Alice's final score.
                    score = min(score, next_dfs)

            memo[key] = score
            return score

        UPPER_BOUND = 10**6
        N = len(piles)
        memo = {}
        return dfs(0, 1, True)


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
        """
        def dfs(start: int, m: int, is_alice: bool) -> int:
            if start == N:
                return 0
            elif memo[is_alice][start][m] != -1:
                return memo[is_alice][start][m]

            score = 0 if is_alice else UPPER_BOUND
            subpile_sum = 0

            for idx in range(start, min(start + 2*m, N)):
                subpile_sum += piles[idx]
                next_dfs = dfs(idx + 1, max(m, idx - start + 1), not is_alice)

                if is_alice:
                    # Alice wants to maximize her final score.
                    score = max(score, subpile_sum + next_dfs)
                else:
                    # Bob wants to minimize Alice's final score.
                    score = min(score, next_dfs)

            memo[is_alice][start][m] = score
            return score

        UPPER_BOUND = 10**6
        N = len(piles)

        if N == 1:
            return piles[0]

        memo = [[[-1] * N for _ in range(N)] for _ in range(2)]
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
        def dfs(start: int, m: int, is_alice: bool) -> int:
            memo_ind = (start, m, is_alice)

            if start == N:
                return 0
            elif memo_ind in memo:
                return memo[memo_ind]

            score = 0 if is_alice else UPPER_BOUND

            for idx in range(start, min(start + 2*m, len(piles))):
                subpile_sum = prefix[idx + 1] - prefix[start]

                next_dfs = dfs(
                    idx + 1,
                    max(m, idx - start + 1),
                    not is_alice
                )

                if is_alice:
                    score = max(score, subpile_sum + next_dfs)
                else:
                    score = min(score, next_dfs)

            memo[memo_ind] = score
            return score

        UPPER_BOUND = 10**6
        N = len(piles)
        memo = {}
        prefix = [0]

        for pile in piles:
            prefix.append(prefix[-1] + pile)

        return dfs(0, 1, True)


print(Solution().stoneGameII([2, 7, 9, 4, 4]) == 10)
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]) == 104)
print(Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]) == 217)
print(Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]) == 98008)
print(Solution().stoneGameII([1]) == 1)
print(Solution().stoneGameII([2, 7]) == 9)
print(Solution().stoneGameII([2, 100]) == 102)
print(Solution().stoneGameII([1, 2, 100]) == 3)
