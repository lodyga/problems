class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^(t/m))
            t: target
            m: min from candidates
        Auxiliary space complexity: O(n)
            n: candidates length
        Tags: backtracking
        """
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
            dfs(index)
            combination.pop()
            dfs(index + 1)

        dfs(0)
        return combination_list


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^(t/m))
            t: target
            m: min from candidates
        Auxiliary space complexity: O(n)
            n: candidates length
        Tags: iterative dfs with backtracking
        """
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
                combination.append(candidates[index])
                dfs(index)
                combination.pop()

        dfs(0)
        return combination_list


print(Solution().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
print(Solution().combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
print(Solution().combinationSum([2], 1), [])