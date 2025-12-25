class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        # [question: maximum points cumulated]
        memo = [-1] * len(questions)

        def dfs(index):
            if index >= len(questions):
                return 0
            elif memo[index] != -1:
                return memo[index]
            
            points, cooldown = questions[index]
            skip = dfs(index + 1)
            solve = points + dfs(index + 1 + cooldown)
            memo[index] = max(skip, solve)
            return memo[index]
        
        return dfs(0)


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: bottom-up
        """
        # [question: maximum points cumulated]
        cache = [0] * len(questions)

        for index in range(len(questions) - 1, -1, -1):
            points, cooldown = questions[index]
            skip = cache[index + 1] if index + 1 < len(questions) else 0
            next_index = index + 1 + cooldown
            solve = points + \
                    (cache[next_index] if next_index < len(questions) else 0)
            cache[index] = max(skip, solve)

        return cache[0]


print(Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5)
print(Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7)
print(Solution().mostPoints([[72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5], [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1], [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2], [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5], [51, 3], [46, 1], [28, 3]]) == 845)
