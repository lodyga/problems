class Solution:
    def sortColors(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
            two pass
        """
        # move zeros left
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # move twos right
        right = len(nums) - 1
        for left in range(right, -1, -1):
            if nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return nums


class Solution:
    def sortColors(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
            two pass
        """
        # move zeros left
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # move ones left
        for right in range(len(nums)):
            if nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bucket sort
            two pass
        """
        bucket = [0] * 3
        for number in nums:
            bucket[number] += 1

        index = 0
        for number, frequency in enumerate(bucket):
            for _ in range(frequency):
                nums[index] = number
                index += 1

        return nums


class Solution:
    def sortColors(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
            one pass
        """
        left = 0
        right = len(nums) - 1
        index = 0

        while index < right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1

            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
                index -= 1

            index += 1

        return nums


print(Solution().sortColors([2, 0, 1]) == [0, 1, 2])
print(Solution().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2])
