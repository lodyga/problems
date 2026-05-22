class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        nums.sort()
        min_val = nums[k - 1] - nums[0]

        for idx in range(k, len(nums) + 1):
            right = idx - 1
            left = idx - k
            min_val = min(min_val, nums[right] - nums[left])

        return min_val


print(Solution().minimumDifference([90], 1) == 0)
print(Solution().minimumDifference([9, 4, 1, 7], 2) == 2)
print(Solution().minimumDifference([9, 4, 1, 7], 3) == 5)
print(Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6) == 74560)
