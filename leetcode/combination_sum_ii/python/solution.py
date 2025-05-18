class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
            n: candidates length
        Tags: backtracking
        """
        candidates.sort()
        combination = []
        combination_list = []

        def dfs(index):
            combination_sum = sum(combination)
            if combination_sum == target:
                combination_list.append(combination.copy())
                return
            elif combination_sum > target or index == len(candidates):
                return

            combination.append(candidates[index])
            dfs(index + 1)
            combination.pop()
            while (index + 1 < len(candidates) and 
                   candidates[index] == candidates[index + 1]):
                index += 1
            dfs(index + 1)

        dfs(0)
        return combination_list


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
            n: candidates length
        Tags: iterative dfs with backtracking
        """
        candidates.sort()
        combination = []
        combination_list = []

        def dfs(start):
            combination_sum = sum(combination)
            if combination_sum == target:
                combination_list.append(combination.copy())
                return
            elif combination_sum > target:
                return

            for index in range(start, len(candidates)):
                if (index > start and 
                        candidates[index] == candidates[index - 1]):
                    continue
                combination.append(candidates[index])
                dfs(index + 1)
                combination.pop()

        dfs(0)
        return combination_list


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
print(Solution().combinationSum2([6], 6), [[6]])
print(Solution().combinationSum2([2, 2, 2], 2), [[2]])