class Solution:
    def isMonotonic(self, nums) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        prev = nums[0]
        is_increasing = True
        is_decreasing = True

        for num in nums:
            if prev > num:
                is_decreasing = False
            if prev < num:
                is_increasing = False
            prev = num

        return is_increasing or is_decreasing


print(Solution().isMonotonic([1, 2, 2, 3]) == True)
print(Solution().isMonotonic([6, 5, 4, 4]) == True)
print(Solution().isMonotonic([1, 3, 2]) == False)
