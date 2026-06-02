class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking
        """
        N = len(nums)

        def backtrack(idx: int, xor: int) -> int:
            if idx == N:
                return xor

            num = nums[idx]
            take = backtrack(idx + 1, xor ^ num)
            skip = backtrack(idx + 1, xor)
            return take + skip

        return backtrack(0, 0)


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking
        """
        N = len(nums)
        res = 0

        def backtrack(idx: int, xor: int) -> None:
            nonlocal res
            if idx == N:
                res += xor
                return

            num = nums[idx]

            # take
            backtrack(idx + 1, xor ^ num)
            # skip
            backtrack(idx + 1, xor)

        backtrack(0, 0)
        return res


print(Solution().subsetXORSum([1, 3]) == 6)
print(Solution().subsetXORSum([5, 1, 6]) == 28)
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]) == 480)
