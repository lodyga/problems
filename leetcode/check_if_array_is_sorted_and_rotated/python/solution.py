class Solution:
    def check(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        is_rotated = False
        for index in range(1, len(nums)):
            if nums[index - 1] <= nums[index]:
                continue

            if is_rotated:
                return False
            else:
                is_rotated = True

        return (
            not is_rotated or
            nums[-1] <= nums[0]
        )


print(Solution().check([3, 4, 5, 1, 2]) == True)
print(Solution().check([2, 1, 3, 4]) == False)
print(Solution().check([1, 2, 3]) == True)
