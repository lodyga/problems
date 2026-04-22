"""
draft
1, 2, 3, 4, 5
2, 3, 4, 5, 1
3, 4, 5, 1, 2
4, 5, 1, 2, 3
5, 1, 2, 3, 4
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left < right:
            # early exit
            if nums[left] < nums[right]:
                # min for [4, 5, 1, 2, 3] case.
                return min(res, nums[left])

            mid = (left + right) // 2
            mid_num = nums[mid]

            if mid_num < nums[right]:
                res = min(res, mid_num)
                right = mid - 1
            else:
                res = min(res, nums[right])
                left = mid + 1

        return res


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left <= right:
            # early exit
            if nums[left] < nums[right]:
                return min(res, nums[left])

            mid = (left + right) // 2
            mid_num = nums[mid]
            res = min(res, mid_num)

            if mid_num < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return res


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search (lower bound)
        """
        left = 0
        right = len(nums) - 1
        min_num = nums[0]

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]
            min_num = min(min_num, mid_num)

            if mid_num < nums[right]:
                right = mid
            else:
                left = mid + 1

        return min_num


print(Solution().findMin([1, 2, 3, 4]) == 1)
print(Solution().findMin([4, 1, 2, 3]) == 1)
print(Solution().findMin([2, 3, 4, 1]) == 1)
print(Solution().findMin([3, 4, 1, 2]) == 1)
print(Solution().findMin([1, 2, 3, 4, 5]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 1, 2, 3]) == 1)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([1]) == 1)
print(Solution().findMin([3, 1, 2]) == 1)
