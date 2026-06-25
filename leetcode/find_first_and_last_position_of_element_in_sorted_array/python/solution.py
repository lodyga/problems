class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        def bisect(nums, target, direction):
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2
                mid_num = nums[mid]

                if target == mid_num:
                    res = mid
                    
                    if direction == "left":
                        right = mid - 1
                    else:  # elif direction == "right":
                        left = mid + 1
                elif target < mid_num:
                    right = mid - 1
                else:
                    left = mid + 1

            return res

        def bisect_left(nums, target):
            return bisect(nums, target, "left")

        def bisect_right(nums, target):
            return bisect(nums, target, "right")

        left_bisect = bisect_left(nums, target)
        right_bisect = bisect_right(nums, target)

        return [left_bisect, right_bisect]


import bisect


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search, build-in function
        """
        if nums == []:
            return [-1, -1]

        low_bisect_idx = bisect.bisect_left(nums, target)

        if low_bisect_idx == len(nums) or nums[low_bisect_idx] != target:
            low_idx = -1
        else:
            low_idx = low_bisect_idx

        high_bisect_idx = bisect.bisect_right(nums, target) - 1

        if high_bisect_idx == -1 or nums[high_bisect_idx] != target:
            high_idx = -1
        else:
            high_idx = high_bisect_idx

        return [low_idx, high_idx]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
print(Solution().searchRange([], 0) == [-1, -1])
print(Solution().searchRange([5, 5, 7], 5) == [0, 1])
print(Solution().searchRange([5, 7, 7], 7) == [1, 2])
print(Solution().searchRange([1], 1) == [0, 0])
print(Solution().searchRange([2, 2], 3) == [-1, -1])

