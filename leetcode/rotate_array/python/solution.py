class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: array
            A: two pointers, in-place method
        """
        def _reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k %= len(nums)
        _reverse(0, len(nums) - k - 1)
        _reverse(len(nums) - k, len(nums) - 1)
        _reverse(0, len(nums) - 1)

        return nums


class Solution:
    def rotate(self, numbers: list[int], k: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: build-in function
        """
        pivot = len(numbers) - k % len(numbers)
        return numbers[pivot:] + numbers[: pivot]


print(Solution().rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
print(Solution().rotate([1, 2, 3], 2) == [2, 3, 1])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([1, 2, 3, 4, 5, 6], 1) == [6, 1, 2, 3, 4, 5])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38) == [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
