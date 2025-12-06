class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original


print(Solution().findFinalValue([5, 3, 6, 1, 12], 3) == 24)
print(Solution().findFinalValue([2, 7, 9], 4) == 4)
