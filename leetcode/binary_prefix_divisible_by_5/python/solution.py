class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: array
            A: iteration
        """
        prefix = 0
        is_divisible = [False] * len(nums)
        for index, num in enumerate(nums):
            prefix = (prefix*2 + num) % 5
            is_divisible[index] = prefix == 0
        return is_divisible


print(Solution().prefixesDivBy5([0, 1, 1]) == [True, False, False])
print(Solution().prefixesDivBy5([1, 1, 1]) == [False, False, False])
print(Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False])
print(Solution().prefixesDivBy5([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]) == [False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False])
