class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: sliding window
        """
        window = 0
        left = 0
        min_length = len(nums) + 1

        for right, num in enumerate(nums):
            window += num

            while window >= target:
                min_length = min(min_length, right - left + 1)
                left_num = nums[left]
                window -= left_num
                left += 1

        return min_length if min_length != len(nums) + 1 else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
print(Solution().minSubArrayLen(4, [1, 4, 4]) == 1)
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0)
