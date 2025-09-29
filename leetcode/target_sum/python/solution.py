class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking, dfs, recursion
        """
        number_counter = len(numbers)

        def dfs(index, total):
            if index == number_counter:
                return total == target

            number = numbers[index]
            # positive number
            possitve = dfs(index + 1, total + number)
            # negative number
            negative = dfs(index + 1, total - number)
            return possitve + negative

        return dfs(0, 0)


class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nm)
            m: sum(numbers)
        Auxiliary space complexity: O(nm)
        Tags: dp, top-down with memoization as hash map
        """
        number_counter = len(numbers)
        memo = {}  # {(index, total): ways to get total using (index + 1) numbers}

        def dfs(index, total):
            if index == number_counter:
                return total == target
            elif (index, total) in memo:
                return memo[(index, total)]

            number = numbers[index]
            # add number
            possitve = dfs(index + 1, total + number)
            # subtract number
            negative = dfs(index + 1, total - number)
            memo[(index, total)] = possitve + negative
            return memo[(index, total)]

        return dfs(0, 0)


from collections import defaultdict


class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nm)
            m: sum(numbers)
        Auxiliary space complexity: O(nm)
        Tags: dp, bottom-up
        """
        number_counter = len(numbers)
        cache = [defaultdict(int) for _ in range(number_counter + 1)]  # [[dict(index, total): counter (ways to get total using `index` numbers), ][index], ]
        cache[0][0] = 1
        
        for index in range(number_counter):
            number = numbers[index]
            for total, counter in cache[index].items():
                cache[index + 1][total + number] += counter
                cache[index + 1][total - number] += counter
        
        return cache[number_counter][target]


class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nm)
            m: sum(numbers)
        Auxiliary space complexity: O(m)
        Tags: dp, bottom-up
        """
        number_counter = len(numbers)
        cache = defaultdict(int)  # [[dict(total): counter (ways to get total using `index` numbers), ], ]
        cache[0] = 1
        
        for index in range(number_counter):
            number = numbers[index]
            next_cache = defaultdict(int)
            for total, counter in cache.items():
                next_cache[total + number] += counter
                next_cache[total - number] += counter
            cache = next_cache
        
        return cache[target]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
print(Solution().findTargetSumWays([2, 2, 2], 2) == 3)
print(Solution().findTargetSumWays([1], 1) == 1)
print(Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) == 5115)