class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        # [day_index: min cost] minimum cost to travel from day dayIndex pointing day onwards
        memo = [-1] * len(days)
        UPPER_COST = len(days) * costs[0]

        def dfs(index):
            if index == len(days):
                return 0
            elif memo[index] != -1:
                return memo[index]

            day = days[index]
            memo[index] = UPPER_COST
            next_index = index

            for cost, validity in zip(costs, (1, 7, 30)):
                while (
                    next_index < len(days) and
                    days[next_index] < day + validity
                ):
                    next_index += 1
                memo[index] = min(memo[index], cost + dfs(next_index))

            return memo[index]

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
        UPPER_COST = len(days) * costs[0]
        # {day_index: cost} minimum cost to travel from day index pointing day onwards
        cache = [UPPER_COST] * (len(days) + 1)
        cache[-1] = 0

        for day_index in range(len(days) - 1, -1, -1):
            for cost, validity in zip(costs, (1, 7, 30)):
                day_index_delta = 1

                while (
                    day_index + day_index_delta < len(days) and
                    days[day_index + day_index_delta] < days[day_index] + validity
                ):
                    day_index_delta += 1

                cache[day_index] = min(
                    cache[day_index],
                    cost + cache[day_index + day_index_delta]
                )

        return cache[0]


print(Solution().mincostTickets([5], [2, 7, 15]) == 2)
print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11)
print(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17)
print(Solution().mincostTickets([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]) == 423)
