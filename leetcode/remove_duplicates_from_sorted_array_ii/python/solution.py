class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 1
        
        for right in range(2, len(nums)):
            if nums[left - 1] == nums[right]:
                continue
            else:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        
        return left + 1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 1

        for right in range(2, len(nums)):
            if nums[left - 1] < nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5)
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7)
