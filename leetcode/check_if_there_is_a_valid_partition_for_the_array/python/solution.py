r"""
draft
                 .
             /        \
            44        444
          /   \      /    \
        .     456   .     .

[4, 4, 4, 5, 6]
[T, F, T, F, F, T]
[1, 1, 1, 2]
[F, F, F, F, T]
"""


class Solution:
    def validPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down witm memoization as hash map
        """
        memo = {len(numbers): True}

        def dfs(index: int) -> bool:
            if index in memo:
                return memo[index]

            memo[index] = False

            # same two digits number
            if not memo[index] and index + 1 < len(numbers):
                if numbers[index] == numbers[index + 1]:
                    memo[index] = dfs(index + 2)

            # same three digits number
            if not memo[index] and index + 2 < len(numbers):
                if numbers[index] == numbers[index + 1] == numbers[index + 2]:
                    memo[index] = dfs(index + 3)

            # ascending by one three digits number
            if not memo[index] and index + 2 < len(numbers):
                if numbers[index] + 2 == numbers[index + 1] + 1 == numbers[index + 2]:
                    memo[index] = dfs(index + 3)

            return memo[index]

        return dfs(0)


class Solution:
    def validPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down witm memoization as array
        """
        memo = [None] * (len(numbers) + 1)
        memo[-1] = True

        def dfs(index: int) -> bool:
            if memo[index]:
                return memo[index]
            elif memo[index] == False:
                return False

            # same two digits number
            if not memo[index] and index + 1 < len(numbers):
                if numbers[index] == numbers[index + 1]:
                    memo[index] = dfs(index + 2)

            # same three digits number
            if not memo[index] and index + 2 < len(numbers):
                if numbers[index] == numbers[index + 1] == numbers[index + 2]:
                    memo[index] = dfs(index + 3)

            # ascending by one three digits number
            if not memo[index] and index + 2 < len(numbers):
                if numbers[index] + 2 == numbers[index + 1] + 1 == numbers[index + 2]:
                    memo[index] = dfs(index + 3)

            memo[index] = True if memo[index] else False
            return memo[index]
        
        return dfs(0)


class Solution:
    def validPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index: int) -> bool:
            if index >= len(numbers):
                return index == len(numbers)

            memo = False

            # same two digits number
            if not memo and index + 1 < len(numbers):
                if numbers[index] == numbers[index + 1]:
                    memo = dfs(index + 2)

            # same three digits number
            if not memo and index + 2 < len(numbers):
                if numbers[index] == numbers[index + 1] == numbers[index + 2]:
                    memo = dfs(index + 3)

            # ascending by one three digits number
            if not memo and index + 2 < len(numbers):
                if numbers[index] + 2 == numbers[index + 1] + 1 == numbers[index + 2]:
                    memo = dfs(index + 3)

            return memo
        
        return dfs(0)


class Solution:
    def validPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [False] * (len(numbers) + 1)
        cache[-1] = True

        for index in reversed(range(len(numbers))):
            # same two digits number
            if not cache[index] and index + 1 < len(numbers):
                if numbers[index] == numbers[index + 1]:
                    cache[index] = cache[index + 2]

            # same three digits number
            if not cache[index] and index + 2 < len(numbers):
                if numbers[index] == numbers[index + 1] == numbers[index + 2]:
                    cache[index] = cache[index + 3]

            # ascending by one three digits number
            if not cache[index] and index + 2 < len(numbers):
                if numbers[index] + 2 == numbers[index + 1] + 1 == numbers[index + 2]:
                    cache[index] = cache[index + 3]

        return cache[0]


class Solution:
    def validPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = [True, True, True, True]

        for index in reversed(range(len(numbers))):
            cache = [False, cache[0], cache[1], cache[2]]

            # same two digits number
            if not cache[0] and index + 1 < len(numbers):
                if numbers[index] == numbers[index + 1]:
                    cache[0] = cache[2]

            # same three digits number
            if not cache[0] and index + 2 < len(numbers):
                if numbers[index] == numbers[index + 1] == numbers[index + 2]:
                    cache[0] = cache[3]

            # ascending by one three digits number
            if not cache[0] and index + 2 < len(numbers):
                if numbers[index] + 2 == numbers[index + 1] + 1 == numbers[index + 2]:
                    cache[0] = cache[3]
            
        return cache[0]


print(Solution().validPartition([4, 4, 4, 5, 6]) == True)
print(Solution().validPartition([1, 1, 1, 2]) == False)
print(Solution().validPartition([993335, 993336, 993337, 993338, 993339, 993340, 993341]) == False)
print(Solution().validPartition([803201, 803201, 803201, 803201, 803202, 803203]) == True)
print(Solution().validPartition([67149, 67149, 67149, 67149, 67149, 136768, 136768, 136768, 136768, 136768, 136768, 136768, 136769, 136770, 136771, 136772, 136773, 136774, 136775, 136776, 136777, 136778, 136779, 136780, 136781, 136782, 136783, 136784]) == False)