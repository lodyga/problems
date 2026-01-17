class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) >> 1
            middle_num = nums[middle]

            if (
                (middle == left or nums[middle - 1] < middle_num) and
                (middle == right or middle_num > nums[middle + 1])
            ):
                return middle
            elif (
                middle == left or
                middle_num < nums[middle + 1]
            ):
                left = middle + 1
            else:
                right = middle - 1
                

print(Solution().findPeakElement([1, 2, 3, 1]) == 2)
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
print(Solution().findPeakElement([1]) == 0)
print(Solution().findPeakElement([1, 2]) == 1)
