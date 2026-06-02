class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: hash map
            A: sliding window
        """
        num_freq = {}
        left = 0
        res = 0

        for right, num in enumerate(nums):
            num_freq[num] = num_freq.get(num, 0) + 1

            while num_freq[num] > k:
                left_num = nums[left]
                num_freq[left_num] -= 1

                if num_freq[num] == 0:
                    num_freq.pop(num)
                
                left += 1

            res = max(res, right - left + 1)

        return res


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6)
print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2)
print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4)
print(Solution().maxSubarrayLength([1, 1, 2], 2) == 3)
print(Solution().maxSubarrayLength([1, 4, 4, 3], 1) == 2)
