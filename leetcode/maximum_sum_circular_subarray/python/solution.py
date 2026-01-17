class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-froce
        """
        N = len(nums)
        max_sub_sum = nums[0]

        for left in range(N):
            total = 0

            for right in range(left, left + N):
                total += nums[right % N]
                max_sub_sum = max(max_sub_sum, total)

        return max_sub_sum


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, Kadane
        """
        N = len(nums)
        total = sum(nums)
        low_sub_sum = 0
        high_sub_sum = 0
        min_sub_sum = nums[0]
        max_sub_sum = nums[0]

        for num in nums:
            high_sub_sum = max(high_sub_sum + num, num)
            max_sub_sum = max(max_sub_sum, high_sub_sum)

            low_sub_sum = min(low_sub_sum + num, num)
            min_sub_sum = min(min_sub_sum, low_sub_sum)

        # If all values are negative: (max_sub_sum < 0) === (total == min_sub_sum)
        if max_sub_sum < 0:
            return max_sub_sum
        else:
            return max(max_sub_sum, total - min_sub_sum)


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]) == 3)
print(Solution().maxSubarraySumCircular([5, -3, 5]) == 10)
print(Solution().maxSubarraySumCircular([-3, -2, -3]) == -2)
print(Solution().maxSubarraySumCircular([-1, -2, -3]) == -1)
print(Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]) == 15)
print(Solution().maxSubarraySumCircular([3, 1, 3, 2, 6]) == 15)
print(Solution().maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]) == 16)
