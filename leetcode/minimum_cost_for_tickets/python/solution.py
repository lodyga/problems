class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        UPPER_BOUND = 365000
        N = len(days)
        VALIDS = [1, 7, 30]
        memo = [-1] * (N + 1)
        memo[-1] = 0

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            res = UPPER_BOUND
            next_idx = idx

            for cost, valid in zip(costs, VALIDS):
                while (
                    next_idx < N
                    and days[next_idx] < days[idx] + valid
                ):
                    next_idx += 1

                res = min(res, cost + dfs(next_idx))

            memo[idx] = res
            return res

        return dfs(0)


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        UPPER_BOUND = 365000
        N = len(days)
        VALIDS = [1, 7, 30]
        cache = [UPPER_BOUND] * (N + 1)
        cache[-1] = 0

        for idx in range(N - 1, -1, -1):
            next_idx = idx

            for cost, valid in zip(costs, VALIDS):
                while (
                    next_idx < N
                    and days[next_idx] < days[idx] + valid
                ):
                    next_idx += 1

                cache[idx] = min(cache[idx], cost + cache[next_idx])

        return cache[0]


print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11)
print(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17)
print(Solution().mincostTickets([5], [2, 7, 15]) == 2)
print(Solution().mincostTickets([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]) == 423)
