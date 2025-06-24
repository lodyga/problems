r"""
draft
                                               1
                      (1,2)/               (7,7)|                 (30,15)\
                         2                     8                         31
          /             |   \               /    |     \
         3              9    32            9    15     39
    /    | \        /   | \
   4    10  33     10   16  39

[1,  4, 6, 7, 8, 20]
[12, 10, 8, 6, 4, 2, 0]
[                   ,  0]
"""


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {day_index: min cost} minimum cost to travel from day index pointing day onwards

        def dfs(day_index):
            if day_index >= len(days):
                return 0
            elif day_index in memo:
                return memo[day_index]

            memo[day_index] = float("inf")

            for cost, validity in zip(costs, (1, 7, 30)):
                day_index_delta = 1

                while (
                    day_index + day_index_delta < len(days) and
                    days[day_index + day_index_delta] < days[day_index] + validity
                ):
                    day_index_delta += 1

                memo[day_index] = min(memo[day_index], 
                                      cost + dfs(day_index + day_index_delta))

            return memo[day_index]

        return dfs(0)


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = [None] * len(days)  # {day_index: cost} minimum cost to travel from day index pointing day onwards


        def dfs(day_index):
            if day_index >= len(days):
                return 0
            elif memo[day_index] is not None:
                return memo[day_index]

            memo[day_index] = float("inf")

            for cost, validity in zip(costs, (1, 7, 30)):
                day_index_delta = 1

                while (day_index + day_index_delta < len(days) and
                       days[day_index + day_index_delta] < days[day_index] + validity):
                    day_index_delta += 1

                memo[day_index] = min(memo[day_index], 
                                      cost + dfs(day_index + day_index_delta))

            return memo[day_index]

        return dfs(0)


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(3^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(day_index):
            if day_index >= len(days):
                return 0

            min_cost = float("inf")

            for cost, validity in zip(costs, (1, 7, 30)):
                day_index_delta = 1

                while (day_index + day_index_delta < len(days) and
                       days[day_index + day_index_delta] < days[day_index] + validity):
                    day_index_delta += 1

                min_cost = min(min_cost, cost + dfs(day_index + day_index_delta))

            return min_cost

        return dfs(0)


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        cache = [float("inf")] * (len(days) + 1)  # {day_index: cost} minimum cost to travel from day index pointing day onwards
        cache[-1] = 0

        for day_index in reversed(range(len(days))):
            for cost, validity in zip(costs, (1, 7, 30)):
                day_index_delta = 1

                while (day_index + day_index_delta < len(days) and
                       days[day_index + day_index_delta] < days[day_index] + validity):
                    day_index_delta += 1

                cache[day_index] = min(cache[day_index], 
                                      cost + cache[day_index + day_index_delta])

        return cache[0]


print(Solution().mincostTickets([5], [2, 7, 15]) == 2)
print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11)
print(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17)
print(Solution().mincostTickets([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]) == 423)