class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = len(scores)
        data = sorted(zip(scores, ages))
        # [starting idx + 1: LIS length]
        memo = [-1] * (N + 1)

        def dfs(idx, prev_idx):
            if idx == N:
                return 0
            elif memo[prev_idx + 1] != -1:
                return memo[prev_idx + 1]

            score, age = data[idx]
            prev_age = -1 if prev_idx == -1 else data[prev_idx][1]

            skip = dfs(idx + 1, prev_idx)
            take = score + dfs(idx + 1, idx) if age >= prev_age else 0

            lis = max(skip, take)
            memo[prev_idx + 1] = lis
            return lis

        return dfs(0, -1)


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(scores)
        data = sorted(zip(scores, ages))
        # [starting index + 1: LIS length]
        cache = [score for score, _ in data]

        for left in range(N - 1, -1, -1):
            score, age = data[left]

            for right in range(left + 1, N):
                next_age = data[right][1]

                if age <= next_age:
                    cache[left] = max(
                        cache[left],
                        score + cache[right]
                    )

        return max(cache)


print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34)
print(Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16)
print(Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6)
print(Solution().bestTeamScore([3, 4], [7, 8]) == 7)
print(Solution().bestTeamScore([4, 3], [7, 8]) == 4)
print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 5, 4, 3]) == 19)
print(Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]) == 29)
print(Solution().bestTeamScore([6, 5, 1, 7, 6, 5, 5, 4, 10, 4], [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]) == 43)
