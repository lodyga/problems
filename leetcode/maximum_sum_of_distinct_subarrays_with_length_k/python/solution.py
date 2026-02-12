class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: hash map
            A: sliding window
        """
        window_num_freq = {}
        window_sum = 0
        left = 0
        res = 0

        for right, num in enumerate(nums):
            window_num_freq[num] = window_num_freq.get(num, 0) + 1
            window_sum += num

            if right < k - 1:
                continue

            if len(window_num_freq) == k:
                res = max(res, window_sum)

            left_num = nums[left]
            window_sum -= left_num
            window_num_freq[left_num] -= 1
            if window_num_freq[left_num] == 0:
                window_num_freq.pop(left_num)
            left += 1

        return res


print(Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15)
print(Solution().maximumSubarraySum([4, 4, 4], 3) == 0)
print(Solution().maximumSubarraySum([9, 9, 9, 1, 2, 3], 3) == 12)
print(Solution().maximumSubarraySum([1, 5, 4, 2, 4, 1, 3], 4) == 12)
