class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 1

        for right in range(1, len(nums)):
            num = nums[right]
            
            if nums[right - 1] != num:
                nums[left] = num
                left += 1

        return left


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0

        for right in range(len(nums)):
            if nums[left] == nums[right]:
                continue
            else:
                left += 1
                nums[left] = nums[right]

        return left + 1


print(Solution().removeDuplicates([1, 1, 2]) == 2)
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
