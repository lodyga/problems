class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: backtracking
        """
        permetation_list = []

        def backtrack(index):
            if index == len(nums):
                permetation_list.append(nums.copy())
                return

            for i2 in range(index, len(nums)):
                nums[index], nums[i2] = nums[i2], nums[index]
                backtrack(index + 1)
                nums[index], nums[i2] = nums[i2], nums[index]

        backtrack(0)
        return permetation_list


print(Solution().permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
print(Solution().permute([0, 1]), [[0, 1], [1, 0]])
print(Solution().permute([1]), [[1]])
