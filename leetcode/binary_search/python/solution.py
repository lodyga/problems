class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if target == mid_num:
                return mid
            elif target < mid_num:
               right = mid - 1
            else:
                left = mid + 1

        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], -1) == 0)
print(Solution().search([-1, 0, 3, 5, 9, 12], 0) == 1)
print(Solution().search([-1, 0, 3, 5, 9, 12], 3) == 2)
print(Solution().search([-1, 0, 3, 5, 9, 12], 5) == 3)
print(Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4)
print(Solution().search([-1, 0, 3, 5, 9, 12], 12) == 5)
print(Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1)
