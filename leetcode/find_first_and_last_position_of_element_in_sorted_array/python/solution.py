class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) - 1
        starting = -1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if target <= mid_num:
                if target == mid_num:
                    starting = mid
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1
        ending = -1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if target >= mid_num:
                if target == mid_num:
                    ending = mid
                left = mid + 1
            else:
                right = mid - 1

        return [starting, ending]


print(Solution().searchRange([5, 5, 7], 5) == [0, 1])
print(Solution().searchRange([5, 7, 7], 7) == [1, 2])
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
print(Solution().searchRange([], 0) == [-1, -1])
print(Solution().searchRange([1], 1) == [0, 0])
