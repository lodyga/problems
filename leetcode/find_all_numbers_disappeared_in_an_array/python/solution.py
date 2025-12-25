class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: negative marking, in-place method
        """
        for num in nums:
            num = abs(num)
            nums[num - 1] = -abs(nums[num - 1])

        return [index + 1 for index, num in enumerate(nums) if num > 0]


print(Solution().findDisappearedNumbers([1, 1]) == [2])
print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
