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
            mid = (left + right) // 2
            mid_num = nums[mid]

            if target == mid_num:
                return mid
            elif target < mid_num:
                right = mid - 1
            else:
                left = mid + 1

        return left


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search, build-in function
        """
        import bisect
        return bisect.bisect_left(nums, target)


print(Solution().searchInsert([1, 3, 5, 6], 1) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 3) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 5) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 6) == 3)
print(Solution().searchInsert([1, 3, 5, 6], 0) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 2) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 4) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 7) == 4)
