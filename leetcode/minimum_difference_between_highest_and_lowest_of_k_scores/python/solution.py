class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        nums.sort()
        min_diff = nums[-1]

        for index in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[index + k - 1] - nums[index])

        return min_diff


print(Solution().minimumDifference([90], 1) == 0)
print(Solution().minimumDifference([9, 4, 1, 7], 2) == 2)
print(Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6) == 74560)
