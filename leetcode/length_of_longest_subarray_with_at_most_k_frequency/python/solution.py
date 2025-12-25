class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags: 
            DS: hash map
            A: sliding window
        """
        window = {}  # {number: frequency}
        left = 0
        window_len = 0

        for right, num in enumerate(nums):
            window[num] = window.get(num, 0) + 1

            while window[num] > k:
                left_num = nums[left]
                window[left_num] -= 1
                if window[left_num] == 0:
                    window.pop(left_num)
                left += 1

            window_len = max(window_len, right - left + 1)

        return window_len


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6)
print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2)
print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4)
print(Solution().maxSubarrayLength([1, 1, 2], 2) == 3)
print(Solution().maxSubarrayLength([1, 4, 4, 3], 1) == 2)
