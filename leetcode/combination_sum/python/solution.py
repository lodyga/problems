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
            backtrack(idx, total + candidate)
            combination.pop()
            backtrack(idx + 1, total)
        
        backtrack(0, 0)
        return res


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
        res = []

        def backtrack(start: int, total: int) -> None:
            if total == target:
                res.append(combination.copy())
                return
            elif total > target:
                return

            for idx in range(start, len(candidates)):
                candidate = candidates[idx]
                combination.append(candidate)
                backtrack(idx, total + candidate)
                combination.pop()

        backtrack(0, 0)
        return res


print(sorted(Solution().combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]]))
print(sorted(Solution().combinationSum([2, 3, 5], 8)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]))
print(sorted(Solution().combinationSum([2], 1)) == sorted([]))
