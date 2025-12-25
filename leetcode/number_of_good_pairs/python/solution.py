class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash map
            A: iteration
        """
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        counter = 0
        for freq in num_freq.values():
            counter += (freq - 1) * freq // 2

        return counter


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4)
print(Solution().numIdenticalPairs([1, 1, 1, 1]) == 6)
print(Solution().numIdenticalPairs([1, 2, 3]) == 0)
