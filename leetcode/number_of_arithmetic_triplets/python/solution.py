class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        num_set = set(nums)
        res = 0

        for num in nums:
            if (
                num - diff in num_set and
                num - diff*2 in num_set
            ):
                res += 1

        return res


print(Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2)
print(Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2)
