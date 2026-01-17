class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^(t/m))
            n: candidates length
            t: target
            m: min from candidates
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []

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
            backtrack(index, total + candidate)
            combination.pop()
            backtrack(index + 1, total)

        backtrack(0, 0)
        return combination_list


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n2^(t/m))
            n: candidates length
            t: target
            m: min from candidates
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []

        def backtrack(index: int, total: int) -> None:
            if total == target:
                combination_list.append(combination.copy())
                return
            elif total > target:
                return

            for i2 in range(index, len(candidates)):
                candidate = candidates[i2]
                combination.append(candidate)
                backtrack(i2, total + candidate)
                combination.pop()

        backtrack(0, 0)
        return combination_list


print(Solution().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
print(Solution().combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
print(Solution().combinationSum([2], 1), [])
