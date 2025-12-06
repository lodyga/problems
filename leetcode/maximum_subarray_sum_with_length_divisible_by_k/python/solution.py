from functools import lru_cache


class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        subarray_sums = [sum(nums[: k])] * len(nums)
        memo = {}

        @lru_cache
        def dfs(index, start, total):
            nonlocal subarray_sums
            if index == len(nums):
                return

            if (index, start, total) in memo:
                return memo[(index, start, total)]

            total += nums[index]

            if (index - start + 1) % k == 0:
                subarray_sums[start] = max(
                    subarray_sums[start],
                    # sum(nums[start: index + 1])
                    total
                )

            # start new subarray
            dfs(index + 1, index + 1, 0)
            # take current number
            dfs(index + 1, start, total)

        dfs(0, 0, 0)
        return max(subarray_sums)


class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        prefix = 0
        subarray_sum = sum(nums[: k])
        # min prefix for every rest: mod = index % k
        min_prefix = [float("inf")] * k
        min_prefix[0] = 0

        for index, num in enumerate(nums, 1):
            prefix += num
            mod = index % k

            if min_prefix[mod] != float("inf"):
                subarray_sum = max(subarray_sum, prefix - min_prefix[mod])

            min_prefix[mod] = min(min_prefix[mod], prefix)

        return subarray_sum


print(Solution().maxSubarraySum([1, 2], 1) == 3)
print(Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4) == -10)
print(Solution().maxSubarraySum([-5, 1, 2, -3, 4], 2) == 4)
print(Solution().maxSubarraySum([9, -11, 15], 2) == 4)
print(Solution().maxSubarraySum([-9653, -7948, -5449, -297, -2536, -2633, -6354, -4335, -5103, -908, -668, -4369, -6986, -328, -3672, -4463, -5360, -5949, -4787, -8946, -7049, -565, -6527, -1386, -1873], 22) == -85094)
