class Solution:
    def subarraySum(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        N = len(nums)
        res = 0

        for left in range(N):
            sub_sum = 0

            for right in range(left, N):
                sub_sum += nums[right]

                if sub_sum == target:
                    res += 1

        return res


class Solution:
    def subarraySum(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: prefix sum
        """
        res = 0
        prefix_freq = {0: 1}
        prefix = 0

        for num in nums:
            prefix += num
            res += prefix_freq.get(prefix - target, 0)
            prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1

        return res


print(Solution().subarraySum([1, 1, 1], 2) == 2)
print(Solution().subarraySum([1, 2, 3], 3) == 2)
print(Solution().subarraySum([1], 0) == 0)
print(Solution().subarraySum([-1, -1, 1], 0) == 1)
print(Solution().subarraySum([1, -1, 1, 1, 1], 2) == 4)
