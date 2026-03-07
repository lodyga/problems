class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        num_freq = {}
        res = -1

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num, freq in num_freq.items():
            if freq == 1:
                res = max(res, num)

        return res


print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8)
print(Solution().largestUniqueNumber([9, 9, 8, 8]) == -1)
