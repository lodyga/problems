r"""
draft
3, 4, 0, 1, 2
4, 0, 1, 2, 3
0, 1, 2, 3, 4

2, 3, 4, 0, 1
1, 2, 3, 4, 0
"""


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: build-in function
        """
        return target in nums


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: almost binary search but not quite
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if target == mid_num:
                return True
            elif nums[left] == mid_num == nums[right]:
                left += 1
                right -= 1
            # right portion is contiguous
            elif mid_num <= nums[right]:
                if mid_num < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # left portion is contiguous
            else:
                if nums[left] <= target < mid_num:
                    right = mid - 1
                else:
                    left = mid + 1

        return False


print(Solution().search([1, 2, 3, 4, 5], 2) == True)
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0) == True)
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3) == False)
print(Solution().search([1], 0) == False)
print(Solution().search([0, 1], 0) == True)
print(Solution().search([1, 0], 0) == True)
print(Solution().search([0, 1], 1) == True)
print(Solution().search([1, 0], 1) == True)
print(Solution().search([0, 1, 1], 0) == True)
print(Solution().search([1, 0, 1, 1, 1], 0) == True)
print(Solution().search([1, 0, 0], 1) == True)
print(Solution().search([1, 2, 1], 1) == True)
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) == True)
