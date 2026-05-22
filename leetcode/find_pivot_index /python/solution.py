class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: prefix sum
        """
        suffix_sum = sum(nums)
        prefix_sum = 0

        for idx, num in enumerate(nums):
            suffix_sum -= num

            if prefix_sum == suffix_sum:
                return idx

            prefix_sum += num

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
print(Solution().pivotIndex([1, 2, 3]) == -1)
print(Solution().pivotIndex([2, 1, -1]) == 0)
