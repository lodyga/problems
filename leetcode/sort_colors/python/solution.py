class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
            two pass
        """
        N = len(nums)
        left = 0

        # Move zeros left.
        for right in range(N):
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # Move ones left after zeros.
        for right in range(N):
            if nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        #_return nums


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
        idx = 0

        for num in nums:
            bucket[num] += 1

        for num, freq in enumerate(bucket):
            for _ in range(freq):
                nums[idx] = num
                idx += 1

        # return nums


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
            one pass
        """
        left = 0
        right = len(nums) - 1
        idx = 0

        while idx <= right:
            if nums[idx] == 1:
                idx += 1

            elif nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1
                idx += 1

            elif nums[idx] == 2:
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1

        # return nums


print(Solution().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2])
print(Solution().sortColors([2, 0, 1]) == [0, 1, 2])
