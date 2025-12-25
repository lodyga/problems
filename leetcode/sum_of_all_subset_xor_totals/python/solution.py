class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: dfs, recursion
        """
        def dfs(index, xor):
            if index == len(nums):
                return xor

            take = dfs(index + 1, xor ^ nums[index])
            skip = dfs(index + 1, xor)
            return take + skip

        return dfs(0, 0)


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: backtracking
        """
        res = 0

        def backtrack(index, xor):
            nonlocal res
            if index == len(nums):
                res += xor
                return

            # take
            backtrack(index + 1, xor ^ nums[index])
            # skip
            backtrack(index + 1, xor)

        backtrack(0, 0)
        return res


print(Solution().subsetXORSum([1, 3]) == 6)
print(Solution().subsetXORSum([5, 1, 6]) == 28)
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]) == 480)
