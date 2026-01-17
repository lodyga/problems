"""
prefix product * postfix product
1 3451, 12 451, 123 51, 1234 1        
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: prefix sum
        """
        postfix = [0] * len(nums)
        postfix[-1] = 1
        
        for index in range(len(nums) - 1, 0, -1):
            num = nums[index]
            postfix[index - 1] = postfix[index] * num

        product = [0] * len(nums)
        prefix = 1
        for index in range(len(nums)):
            product[index] = prefix * postfix[index]
            num = nums[index]
            prefix *= num

        return product


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: prefix sum
        """
        postfix = [0] * len(nums)
        postfix[-1] = 1

        for index in range(len(nums) - 1, 0, -1):
            num = nums[index]
            postfix[index - 1] = postfix[index] * num

        prefix = 1
        for index in range(len(nums)):
            postfix[index] *= prefix
            num = nums[index]
            prefix *= num

        return postfix


print(Solution().productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24])
print(Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
