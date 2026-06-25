class Solution:
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        """
        Time complexity: O(log(n))
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search

        Starts with `window` positioned in the middle of the `nums`.
        Start binary search. If the first number outside of the `window` 
        on the right minus `x` is less than `x` minus the first character 
        in the `window` then search the right portion of the binary search.
        The solution on the right would be better than current `window`.
        Else search the left portion of the binary search while preserving current 
        `window` (current `window` could be the solution).
        """
        N = len(nums)
        left = 0
        right = N - k

        while left < right:
            mid = (left + right) // 2

            if target - nums[mid] <= nums[mid + k] - target:
                right = mid - 1
            else:
                left = mid + 1

        return nums[left: left + k]


class Solution:
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0
        right = len(nums) - 1

        while right - left + 1 > k:
            if target - nums[left] <= nums[right] - target:
                right -= 1
            else:
                left += 1

        return nums[left: left + k]


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4])
print(Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3])
print(Solution().findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9) == [3, 6, 8, 8, 9])
