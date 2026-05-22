class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        left = 0
        window_sum = 0
        N = len(nums)
        res = N + 1

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return res if res < N + 1 else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
print(Solution().minSubArrayLen(4, [1, 4, 4]) == 1)
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0)
