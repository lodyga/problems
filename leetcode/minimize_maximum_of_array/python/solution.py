class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy, prefix sum
        """
        max_value = nums[0]
        prefix = 0

        for index, num in enumerate(nums):
            prefix += num
            if num <= max_value:
                continue

            max_value = max(max_value, (prefix - 1) // (index + 1) + 1)

        return max_value


print(Solution().minimizeArrayValue([3, 7, 1, 6]) == 5)
print(Solution().minimizeArrayValue([10, 1]) == 10)
print(Solution().minimizeArrayValue([13, 13, 20, 0, 8, 9, 9]) == 16)
