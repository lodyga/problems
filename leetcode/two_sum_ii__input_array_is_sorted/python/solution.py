class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            pair = nums[left] + nums[right]

            if pair == target:
                return [left + 1, right + 1]
            elif pair < target:
                left += 1
            else:
                right -= 1


print(Solution().twoSum([2, 7, 11, 15], 9) == [1, 2])
print(Solution().twoSum([2, 3, 4], 6) == [1, 3])
print(Solution().twoSum([-1, 0], -1) == [1, 2])
