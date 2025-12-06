class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        num_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], index]
            else:
                num_index[num] = index


print(Solution().twoSum([2, 7, 11, 15], 9) == [0, 1])
print(Solution().twoSum([3, 2, 4], 6) == [1, 2])
print(Solution().twoSum([3, 3], 6) == [0, 1])
