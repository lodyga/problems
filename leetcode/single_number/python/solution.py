class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor


print(Solution().singleNumber([2, 2, 1]) == 1)
print(Solution().singleNumber([4, 1, 2, 1, 2]) == 4)
print(Solution().singleNumber([1]) == 1)
