class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bit manipulation, prefix sum
        """
        k = (1 << maximumBit) - 1
        xor = 0
        res = []

        for num in nums:
            xor ^= num
            res.append(xor ^ k)

        return res[::-1]


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bit manipulation, prefix sum
        """
        k = (1 << maximumBit) - 1
        xor = 0
        res = []

        for num in nums:
            xor ^= num

        for num in reversed(nums):
            res.append(xor ^ k)
            xor ^= num

        return res


print(Solution().getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3])
print(Solution().getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5])
print(Solution().getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7])
