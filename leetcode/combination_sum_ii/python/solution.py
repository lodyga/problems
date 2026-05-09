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
        N = len(candidates)
        combination = []
        res = []

        def backtrack(idx: int, total: int) -> None:
            if total == target:
                res.append(combination.copy())
                return
            if (
                total > target or
                idx == N
            ):
                return

            candidate = candidates[idx]
            combination.append(candidate)
            backtrack(idx + 1, total + candidate)
            combination.pop()

            while (
                idx + 1 < N and
                candidates[idx] == candidates[idx + 1]
            ):
                idx += 1

            backtrack(idx + 1, total)

        backtrack(0, 0)
        return res


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
        res = []

        def backtrack(start: int, total: int) -> None:
            if total == target:
                res.append(combination.copy())
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
        return res


print(sorted(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]))
print(sorted(Solution().combinationSum2([2, 5, 2, 1, 2], 5)) == sorted([[1, 2, 2], [5]]))
print(sorted(Solution().combinationSum2([6], 6)) == sorted([[6]]))
print(sorted(Solution().combinationSum2([2, 2, 2], 2)) == sorted([[2]]))
