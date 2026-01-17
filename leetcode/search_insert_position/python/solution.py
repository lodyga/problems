import bisect


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
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
            elif target < middle_num:
                right = middle - 1
            else:
                left = middle + 1

        return left


    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


print(Solution().searchInsert([1, 3, 5, 6], 1) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 3) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 5) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 6) == 3)
print(Solution().searchInsert([1, 3, 5, 6], 0) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 2) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 4) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 7) == 4)
