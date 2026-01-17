class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: prefix sum
        """
        prefix = 0
        suffix = sum(nums)

        for index, num in enumerate(nums):
            suffix -= num
            if prefix == suffix:
                return index
            prefix += num

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
print(Solution().pivotIndex([1, 2, 3]) == -1)
print(Solution().pivotIndex([2, 1, -1]) == 0)
