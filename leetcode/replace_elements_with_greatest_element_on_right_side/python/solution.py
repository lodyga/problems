class Solution:
    def replaceElements(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        prev = -1
        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            next = max(prev, num)
            nums[index] = prev
            prev = next

        return nums


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1])
print(Solution().replaceElements([400]) == [-1])
