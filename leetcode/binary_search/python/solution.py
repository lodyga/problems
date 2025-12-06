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
            elif target < middle_num:
                right = middle - 1
            else:
                left = middle + 1

        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], -1) == 0)
print(Solution().search([-1, 0, 3, 5, 9, 12], 0) == 1)
print(Solution().search([-1, 0, 3, 5, 9, 12], 3) == 2)
print(Solution().search([-1, 0, 3, 5, 9, 12], 5) == 3)
print(Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4)
print(Solution().search([-1, 0, 3, 5, 9, 12], 12) == 5)
print(Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1)
