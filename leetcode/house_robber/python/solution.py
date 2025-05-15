# draft
# values     [2, 7, 9,  3,  1]
# cumulative [2, 7, 11,11. 12]

# [2, 100, 9, 3, 100] data
# [2, 100, 100, 100, 200] dp solution
# [(2), (2, 100), (100, 100) ....]

# [100, 9, 3, 100, 2] data
# [100, 100, 100, 200, 200] dp solution


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        if len(numbers) <= 2:
            return max(numbers)

        cache = (numbers[0], max(numbers[:2]))

        for number in numbers[2:]:
            cache = (cache[1], max(cache[0] + number, cache[1]))

        return cache[1]


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        mutate input list
        """
        if len(numbers) <= 2:
            return max(numbers)

        numbers[1] = max(numbers[:2])

        for index, number in enumerate(numbers[2:], 2):
            numbers[index] = max(numbers[index - 2] +
                                 number, numbers[index - 1])

        return numbers[-1]


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        if len(numbers) <= 2:
            return max(numbers)

        cache = [0] * len(numbers)
        cache[0] = numbers[0]
        cache[1] = max(numbers[:2])

        for index, number in enumerate(numbers[2:], 2):
            cache[index] = max(cache[index - 2] + number, cache[index - 1])

        return cache[-1]


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {
            len(numbers): 0,
            len(numbers) + 1: 0
        }

        def dfs(index):
            if index in memo:
                return memo[index]

            memo[index] = max(numbers[index] + dfs(index + 2),
                              dfs(index + 1))

            return memo[index]

        return dfs(0)


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        memo = [None] * (len(numbers) + 2)
        memo[-1] = 0
        memo[-2] = 0

        def dfs(index):
            if memo[index] is not None:
                return memo[index]

            memo[index] = max(numbers[index] + dfs(index + 2),
                              dfs(index + 1))

            return memo[index]

        return dfs(0)


class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index):
            if index >= len(numbers):
                return 0

            return max(numbers[index] + dfs(index + 2),
                       dfs(index + 1))

        return dfs(0)


print(Solution().rob([2]) == 2)
print(Solution().rob([0]) == 0)
print(Solution().rob([2, 1]) == 2)
print(Solution().rob([2, 100, 9, 3, 100]) == 200)
print(Solution().rob([100, 9, 3, 100, 2]) == 200)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([2, 7, 9, 3, 1]) == 12)
print(Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) == 3365)
print(Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0)