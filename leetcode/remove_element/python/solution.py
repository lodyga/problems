class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, in-place method
        """
        left = 0

        for right, number in enumerate(nums):
            if number != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return left


print(Solution().removeElement([3, 2, 2, 3], 3) == 2)
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5)