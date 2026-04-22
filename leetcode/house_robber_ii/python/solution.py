class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        if len(nums) <= 3:
            return max(nums)

        def one_rob(nums):
            N = len(nums)
            if N <= 2:
                return max(nums)

            cache = [0, 0]

            for idx in range(N - 1, -1, -1):
                num = nums[idx]
                cache[0], cache[1] = max(cache[0], num + cache[1]), cache[0]

            return cache[0]

        return max(one_rob(nums[: -1]),
                   one_rob(nums[1:]))


print(Solution().rob([2, 3, 2]) == 3)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([1, 2, 3]) == 3)
print(Solution().rob([1]) == 1)
print(Solution().rob([0, 0]) == 0)
print(Solution().rob([1, 3, 1, 3, 100]) == 103)
