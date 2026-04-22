class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: prefix sum
        """
        res = [1]
        suffix = 1

        for idx in range(len(nums) - 1):
            num = nums[idx]
            res.append(res[-1] * num)

        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= suffix
            suffix *= nums[idx]

        return res


print(Solution().productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24])
print(Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
