r"""
draft
if middle < right: right portion is contiguous
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
            middle = (left + right) >> 1
            middle_num = nums[middle]

            if target == middle_num:
                return middle
            # right side portion is contiguous
            elif middle_num < nums[right]:
                if middle_num < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # left side portion is contiguous
            else:
                if nums[left] <= target < middle_num:
                    right = middle - 1
                else:
                    left = middle + 1

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
