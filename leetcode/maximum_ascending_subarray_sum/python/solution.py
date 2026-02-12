class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        prev_num = nums[0] - 1
        max_sum = 0
        curr_sum = 0

        for num in nums:
            if prev_num < num:
                curr_sum += num
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = num

            prev_num = num

        return max_sum


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        prev_num = nums[0] - 1
        max_sum = 0
        curr_sum = 0

        for num in nums:
            if prev_num >= num:
                curr_sum = 0

            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            prev_num = num

        return max_sum


print(Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65)
print(Solution().maxAscendingSum([10, 20, 30, 40, 50]) == 150)
print(Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33)
