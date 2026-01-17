class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


print(Solution().moveZeroes([0]), [0])
print(Solution().moveZeroes([1]), [1])
print(Solution().moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
