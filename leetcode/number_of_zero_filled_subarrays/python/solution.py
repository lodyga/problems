"""
1: 1 = 1
2: 3 = 2 + 1
3: 6 = 3 + 2 + 1
"""


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        left = 0
        counter = 0
        nums.append(-1)

        for right, num in enumerate(nums):
            if num != 0:
                counter += (1 + (right - left)) * (right - left) // 2
                left = right + 1

        return counter


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        zeros = 0
        counter = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                zeros = 0
            counter += zeros
        return counter


print(Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6)
print(Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9)
print(Solution().zeroFilledSubarray([2, 10, 2019]) == 0)
