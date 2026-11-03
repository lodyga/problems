class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-froce
        """
        N = len(nums)
        res = nums[0]

        for idx in range(N):
            curr_sum = 0

            for jdx in range(idx, N + idx):
                curr_sum += nums[jdx % N]
                res = max(res, curr_sum)

        return res


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        total = sum(nums)
        local_max_sum = 0
        local_min_sum = 0
        global_max_sum = nums[0]
        global_min_sum = nums[0]

        for num in nums:
            local_max_sum = max(local_max_sum + num, num)
            global_max_sum = max(global_max_sum, local_max_sum)

            local_min_sum = min(local_min_sum + num, num)
            global_min_sum = min(global_min_sum, local_min_sum)

        # If all values are negative: (global_max_sum < 0) === (total == global_min_sum)
        if global_max_sum > 0:
            return max(global_max_sum, total - global_min_sum)
        else:
            return global_max_sum


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]) == 3)
print(Solution().maxSubarraySumCircular([5, -3, 5]) == 10)
print(Solution().maxSubarraySumCircular([-3, -2, -3]) == -2)
print(Solution().maxSubarraySumCircular([-1, -2, -3]) == -1)
print(Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]) == 15)
print(Solution().maxSubarraySumCircular([3, 1, 3, 2, 6]) == 15)
print(Solution().maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]) == 16)
