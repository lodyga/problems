r"""
draft
if mid < right: right portion is contiguous
[1, 2, 3, 4, 5]
[4, 5, 1, 2, 3]
[5, 1, 2, 3, 4]

[2, 3, 4, 5, 1]
[3, 4, 5, 1, 2]
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
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

            if target == mid_num:
                return mid
            # The right side portion is contiguous.
            elif mid_num < nums[right]:
                if mid_num < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # The left side portion is contiguous.
            else:
                if nums[left] <= target < mid_num:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


print(Solution().search([1, 3, 5], 5) == 2)
print(Solution().search([3, 5, 1], 3) == 0)
print(Solution().search([3, 5, 1], 1) == 2)
print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4)
print(Solution().search([5, 1, 3], 3) == 2)
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
print(Solution().search([1], 0) == -1)
print(Solution().search([5, 1, 3], 4) == -1)
print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4)
