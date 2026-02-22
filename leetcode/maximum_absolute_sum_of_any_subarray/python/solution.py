class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy (Kadane)
        """
        positive_sum = 0
        max_positive = nums[0]

        negative_sum = 0
        min_negative = nums[0]

        for num in nums:
            positive_sum = max(positive_sum + num, num)
            max_positive = max(max_positive, positive_sum)

            negative_sum = min(negative_sum + num, num)
            min_negative = min(min_negative, negative_sum)

        return max(max_positive, -min_negative)


print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) == 5)
print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8)
print(Solution().maxAbsoluteSum([-1, 5]) == 5)
