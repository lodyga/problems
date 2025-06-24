class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        # [question: maximum points cumulated]
        memo = [None] * len(questions)

        def dfs(index):
            if index >= len(questions):
                return 0
            elif memo[index] is not None:
                return memo[index]

            points, brainpower = questions[index]

            memo[index] = max(
                # solve question
                points + dfs(index + brainpower + 1),
                # skip question
                dfs(index + 1)
            )

            return memo[index]

        return dfs(0)


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        # [question: maximum points cumulated]
        memo = {}

        def dfs(index):
            if index >= len(questions):
                return 0
            elif index in memo:
                return memo[index]

            points, brainpower = questions[index]
            memo[index] = max(
                # solve question
                points + dfs(index + brainpower + 1),
                # skip question
                dfs(index + 1)
            )

            return memo[index]

        return dfs(0)


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index):
            if index >= len(questions):
                return 0

            points, brainpower = questions[index]
            memo = max(
                # solve question
                points + dfs(index + brainpower + 1),
                # skip question
                dfs(index + 1)
            )

            return memo

        return dfs(0)


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as array
        """
        # [question: maximum points cumulated]
        cache = [0] * (len(questions) + 1)
        cache[-1] = 0

        for index in reversed(range(len(questions))):
            points, brainpower = questions[index]
            skip = index + brainpower + 1
            
            if skip < len(questions):
                cache[index] = max(cache[index + 1], points + cache[skip])
            else:
                cache[index] = max(cache[index + 1], points + 0)

        return cache[0]


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with tabulation as hash map
        """
        # [question: maximum points cumulated]
        cache = {}
        cache[len(questions)] = 0

        for index in reversed(range(len(questions))):
            points, brainpower = questions[index]
            skip = index + brainpower + 1
            
            if skip < len(questions):
                cache[index] = max(cache[index + 1], points + cache[skip])
            else:
                cache[index] = max(cache[index + 1], points + 0)

        return cache[0]


print(Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5)
print(Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7)
print(Solution().mostPoints([[72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5], [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1], [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2], [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5], [51, 3], [46, 1], [28, 3]]) == 845)