class Solution:
    def subarraySum(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        counter = 0
        for left in range(len(nums)):
            sub_sum = 0
            for right in range(left, len(nums)):
                sub_sum += nums[right]
                counter += 1 if sub_sum == target else 0

        return counter


class Solution:
    def subarraySum(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: prefix sum
        """
        counter = 0
        prefix = 0
        prefix_freq = {0: 1}

        for num in nums:
            prefix += num
            counter += prefix_freq.get(prefix - target, 0)
            prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1

        return counter


print(Solution().subarraySum([1, 1, 1], 2) == 2)
print(Solution().subarraySum([1, 2, 3], 3) == 2)
print(Solution().subarraySum([1], 0) == 0)
print(Solution().subarraySum([-1, -1, 1], 0) == 1)
print(Solution().subarraySum([1, -1, 1, 1, 1], 2) == 4)
