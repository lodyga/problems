class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        res = nums[0]
        sub_sum = 0

        for num in nums:
            sub_sum = sub_sum + num if sub_sum > 0 else num
            res = max(res, sub_sum)

        return res


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([5, 4, -1, 7, 8]) == 23)
print(Solution().maxSubArray([-4, -2, -1, -3]) == -1)
