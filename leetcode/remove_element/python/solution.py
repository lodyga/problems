class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
        """
        left = 0
        
        for right, num in enumerate(nums):
            if num != val:
                nums[left], nums[right] = num, nums[left]
                left += 1

        return left


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
        """
        left = len(nums) - 1

        for right in range(len(nums) - 1, -1, -1):
            if nums[right] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left -= 1

        return left + 1


print(Solution().removeElement([3, 2, 2, 3], 3) == 2)
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5)
