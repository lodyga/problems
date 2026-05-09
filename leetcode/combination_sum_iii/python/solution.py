class Solution:
    def combinationSum3(self, k: int, target: int) -> list[list[int]]:
        """
        Time complexity: O(1)
            O(2^9)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        res = []
        combination = []

        def backtrack(num: int, total: int) -> None:
            if len(combination) == k:
                if total == target:
                    res.append(combination.copy())
                return
            elif total >= target or num == 10:
                return

            combination.append(num)
            backtrack(num + 1, total + num)
            combination.pop()
            backtrack(num + 1, total)

        backtrack(1, 0)
        return res


class Solution:
    def combinationSum3(self, k: int, target: int) -> list[list[int]]:
        """
        Time complexity: O(1)
            O(2^9)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        res = []
        combination = []

        def backtrack(num: int, total: int) -> None:
            if len(combination) == k:
                if total == target:
                    res.append(combination.copy())
                return
            elif total >= target or num == 10:
                return

            for idx in range(num, 10):
                combination.append(idx)
                backtrack(idx + 1, total + idx)
                combination.pop()

        backtrack(1, 0)
        return res


print(Solution().combinationSum3(2, 4) == [[1, 3]])
print(Solution().combinationSum3(3, 7) == [[1, 2, 4]])
print(Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
print(Solution().combinationSum3(4, 1) == [])
