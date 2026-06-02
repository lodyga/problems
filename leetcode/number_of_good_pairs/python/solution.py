class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: prefix sum
        """
        num_freq = {}
        res = 0

        for num in nums:
            if num in num_freq:
                res += num_freq[num]
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        return res


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
        res = 0

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for freq in num_freq.values():
            res += (freq - 1) * freq // 2

        return res


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4)
print(Solution().numIdenticalPairs([1, 1, 1, 1]) == 6)
print(Solution().numIdenticalPairs([1, 2, 3]) == 0)
