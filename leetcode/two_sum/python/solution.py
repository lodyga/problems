class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        num_idx = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in num_idx:
                return [num_idx[diff], idx]
            else:
                num_idx[num] = idx


print(Solution().twoSum([2, 7, 11, 15], 9) == [0, 1])
print(Solution().twoSum([3, 2, 4], 6) == [1, 2])
print(Solution().twoSum([3, 3], 6) == [0, 1])
