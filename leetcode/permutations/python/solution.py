class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: backtracking
        """
        N = len(nums)
        res = []

        def backtrack(start: int) -> None:
            if start == N:
                res.append(nums.copy())
                return

            for idx in range(start, N):
                nums[start], nums[idx] = nums[idx], nums[start]
                backtrack(start + 1)
                nums[start], nums[idx] = nums[idx], nums[start]

        backtrack(0)
        return res


print(sorted(Solution().permute([1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
print(sorted(Solution().permute([0, 1])) == sorted([[0, 1], [1, 0]]))
print(sorted(Solution().permute([1])) == sorted([[1]]))
