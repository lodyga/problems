class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing stack
            A: iteration
        """
        stack = []
        res = 0

        for index, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(index)

        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]

            while stack and nums[stack[-1]] <= num:
                res = max(res, index - stack[-1])
                stack.pop()

        return res


print(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4)
print(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7)
print(Solution().maxWidthRamp([8, 6, 0, 8, 2, 7, 7]) == 5)
