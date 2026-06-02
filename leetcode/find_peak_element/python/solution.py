class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        N = len(nums)
        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if (
                (mid == 0 and (mid + 1 == N or mid_num > nums[mid + 1])) or
                (mid == N - 1 and nums[mid - 1] < mid_num) or
                nums[mid - 1] < mid_num > nums[mid + 1]
            ):
                return mid
            elif mid + 1 < N and mid_num < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1


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
            mid = (left + right) // 2
            mid_num = nums[mid]

            if (
                (mid == left or nums[mid - 1] < mid_num) and
                (mid == right or mid_num > nums[mid + 1])
            ):
                return mid
            elif (
                mid == left or
                mid_num < nums[mid + 1]
            ):
                left = mid + 1
            else:
                right = mid - 1
                

print(Solution().findPeakElement([1, 2, 3, 1]) == 2)
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
print(Solution().findPeakElement([1]) == 0)
print(Solution().findPeakElement([1, 2]) == 1)
