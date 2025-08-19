class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(ns)
            O(s): sum(numbers)
        Auxiliary space complexity: O(ns)
        Tags: dp, top-down with memoization as hash map
        """
        numbers_length = len(numbers)
        memo = {}  # {(index, current sum): expressions count}

        def dfs(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            elif index == numbers_length:
                return 1 if current_sum == target else 0

            # positive number
            possitve = dfs(index + 1, current_sum + numbers[index])
            # negative number
            negative = dfs(index + 1, current_sum - numbers[index])
            memo[(index, current_sum)] = possitve + negative
            return memo[(index, current_sum)]

        return dfs(0, 0)


class Solution:
    def findTargetSumWays(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking, dfs, recursion
        """
        numbers_length = len(numbers)

        def dfs(index, current_sum):
            if index == numbers_length:
                return 1 if current_sum == target else 0

            # positive number
            possitve = dfs(index + 1, current_sum + numbers[index])
            # negative number
            negative = dfs(index + 1, current_sum - numbers[index])
            return possitve + negative

        return dfs(0, 0)


print(Solution().findTargetSumWays([2, 2, 2], 2) == 3)
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
print(Solution().findTargetSumWays([1], 1) == 1)
print(Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) == 5115)