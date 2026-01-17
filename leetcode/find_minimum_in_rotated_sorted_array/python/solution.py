"""
draft
1, 2, 3, 4, 5
4, 5, 1, 2, 3
5, 1, 2, 3, 4

2, 3, 4, 5, 1
3, 4, 5, 1, 2
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
        min_num = nums[0]

        while left <= right:
            # early exit
            if nums[left] < nums[right]:
                return min(min_num, nums[left])

            middle = (left + right) >> 1
            middle_num = nums[middle]
            min_num = min(min_num, middle_num)

            if middle_num < nums[right]:
                right = middle - 1
            else:
                left = middle + 1

        return min_num

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
            middle = (left + right) >> 1
            middle_num = nums[middle]
            min_num = min(min_num, middle_num)

            if middle_num < nums[right]:
                right = middle
            else:
                left = middle + 1

        return min_num


print(Solution().findMin([1, 2, 3, 4]) == 1)
print(Solution().findMin([4, 1, 2, 3]) == 1)
print(Solution().findMin([2, 3, 4, 1]) == 1)
print(Solution().findMin([3, 4, 1, 2]) == 1)
print(Solution().findMin([4, 5, 1, 2, 3]) == 1)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([1, 2, 3, 4, 5]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([1]) == 1)
print(Solution().findMin([3, 1, 2]) == 1)
