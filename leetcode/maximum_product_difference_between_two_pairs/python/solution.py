class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        mins = [10**5, 10**5]
        maxs = [0, 0]

        for num in nums:
            if num < mins[0]:
                mins[1] = mins[0]
                mins[0] = num
            elif num < mins[1]:
                mins[1] = num

            if num > maxs[0]:
                maxs[1] = maxs[0]
                maxs[0] = num
            elif num > maxs[1]:
                maxs[1] = num

        return maxs[0] * maxs[1] - mins[0] * mins[1]


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting, build-in function
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


print(Solution().maxProductDifference([5, 6, 2, 7, 4]) == 34)
print(Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]) == 64)
