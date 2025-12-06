class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
            n: candidates length
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []
        candidates.sort()

        def backtrack(index: int, total: int) -> None:
            if total == target:
                combination_list.append(combination.copy())
                return
            elif (
                total > target or
                index == len(candidates)
            ):
                return

            candidate = candidates[index]
            combination.append(candidate)
            backtrack(index + 1, total + candidate)
            combination.pop()
            while (
                index + 1 < len(candidates) and
                candidates[index] == candidates[index + 1]
            ):
                index += 1
            backtrack(index + 1, total)

        backtrack(0, 0)
        return combination_list


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
            n: candidates length
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: DFS with backtracking
        """
        candidates.sort()
        combination = []
        combination_list = []

        def backtrack(start: int, total: int) -> None:
            if total == target:
                combination_list.append(combination.copy())
                return
            elif total > target:
                return

            for index in range(start, len(candidates)):
                if (
                    index > start and 
                    candidates[index] == candidates[index - 1]
                ):
                    continue
                candidate = candidates[index]
                combination.append(candidate)
                backtrack(index + 1, total + candidate)
                combination.pop()

        backtrack(0, 0)
        return combination_list


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
print(Solution().combinationSum2([6], 6), [[6]])
print(Solution().combinationSum2([2, 2, 2], 2), [[2]])
