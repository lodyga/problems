class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index, alice_to_move, m):
            if index >= len(piles):
                return 0

            score = 0 if alice_to_move else 10**6
            subpile_sum = 0
            # for x in range(1, 2*m + 1):
            for j in range(index, min(index + 2*m, len(piles))):
                subpile_sum += piles[j]
                if alice_to_move:
                    ponits = subpile_sum + dfs(j + 1, not alice_to_move, max(m, j - index + 1))
                    score = max(score, ponits)
                else:
                    ponits = dfs(j + 1, not alice_to_move, max(m, j - index + 1))
                    score = min(score, ponits)
            return score
        return dfs(0, True, 1)


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index, alice_to_move, m):
            if index >= len(piles):
                return 0

            score = 0 if alice_to_move else 10**6
            subpile_sum = 0
            for x in range(1, 2*m + 1):
                if index + x > len(piles):
                    break
                subpile_sum += piles[index + x - 1]
                if alice_to_move:
                    ponits = subpile_sum + dfs(index + x, not alice_to_move, max(m, x))
                    score = max(score, ponits)
                else:
                    ponits = dfs(index + x, not alice_to_move, max(m, x))
                    score = min(score, ponits)
            return score
        return dfs(0, True, 1)


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Time complexity: O(n3)

        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index, alice_to_move, m): alice's max score}

        def dfs(index, alice_to_move, m):
            if index == len(piles):
                return 0
            elif (index, alice_to_move, m) in memo:
                return memo[(index, alice_to_move, m)]

            # result max wihile Alice, min while Bob
            memo[(index, alice_to_move, m)] = 0 if alice_to_move else 10**6
            part_sum = 0

            for x in range(1, 2*m + 1):
                if index + x - 1 == len(piles):
                    break
                part_sum += (piles[index + x - 1] if alice_to_move else 0)
                score = part_sum + dfs(index + x, not alice_to_move, max(m, x))
                # score = (sum(piles[index: index + x]) if alice_to_move else 0) + \
                #     dfs(index + x, not alice_to_move, max(m, x))
                memo[(index, alice_to_move, m)] = (
                    max(memo[(index, alice_to_move, m)], score) if alice_to_move else
                    min(memo[(index, alice_to_move, m)], score)
                )

            return memo[(index, alice_to_move, m)]

        return dfs(0, True, 1)


print(Solution().stoneGameII([2, 7]), 9)
print(Solution().stoneGameII([2, 7, 9, 4, 4]), 10)
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]), 104)
print(Solution().stoneGameII([2, 100]), 102)
print(Solution().stoneGameII([1, 2, 100]), 3)
print(Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]), 217)
print(Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]), 98008)