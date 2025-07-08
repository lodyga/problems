class Solution:
    def jump(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        jump_counter = 0
        left = 0
        right = 0

        while right < len(numbers) - 1:
            next_right = 0

            for index in range(left, right + 1):
                next_right = max(next_right, index + numbers[index])
            
            left = right + 1
            right = next_right
            jump_counter += 1

        return jump_counter


class Solution:
    def jump(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [len(numbers)] * len(numbers)
        cache[-1] = 0

        for index in reversed(range(len(numbers) - 1)):
            if numbers[index] == 0:
                cache[index] = len(numbers)

            for i in range(index + 1, index + numbers[index] + 1):
                if i < len(numbers):
                    cache[index] = min(cache[index], cache[i] + 1)

        return cache[0]


class Solution:
    def jump(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = [None] * len(numbers)
        memo[-1] = 0

        def dfs(index):
            if index > len(numbers) - 1:
                return len(numbers)
            elif memo[index] is not None:
                return memo[index]
            elif numbers[index] > 0:
                memo[index] = min(
                    dfs(index + i) + 1
                    for i in range(1, numbers[index] + 1)
                )
                return memo[index]
            else:
                return len(numbers)

        dfs(0)
        return memo[0]


class Solution:
    def jump(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index):
            if index == len(numbers) - 1:
                return 0
            elif index > len(numbers) - 1:
                return len(numbers)

            if numbers[index] > 0:
                return min(
                    dfs(index + i) + 1
                    for i in range(1, numbers[index] + 1)
                )
            else:
                return len(numbers)

        return dfs(0)


print(Solution().jump([2, 3, 1, 1, 4]) == 2)
print(Solution().jump([2, 3, 0, 1, 4]) == 2)
print(Solution().jump([0]) == 0)
print(Solution().jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]) == 5)