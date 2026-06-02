class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        def is_weakly_increasing(nums: list[int]) -> bool:
            prev_num = nums[0] - 1

            for num in nums:
                if prev_num > num:
                    return False

                prev_num = num

            return True

        def is_weakly_decreasing(nums: list[int]) -> bool:
            prev_num = nums[0] + 1

            for num in nums:
                if prev_num < num:
                    return False

                prev_num = num

            return True

        return (
            is_weakly_increasing(nums)
            or is_weakly_decreasing(nums)
        )


print(Solution().isMonotonic([1, 2, 2, 3]) == True)
print(Solution().isMonotonic([6, 5, 4, 4]) == True)
print(Solution().isMonotonic([1, 3, 2]) == False)
