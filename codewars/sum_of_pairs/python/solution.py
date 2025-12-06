class Solution:
    def sum_pairs(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        num_set = set()
        for num in nums:
            complement = target - num
            if complement in num_set:
                return [complement, num]
            else:
                num_set.add(num)
        return []


print(Solution().sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7])
print(Solution().sum_pairs([1, 4, 8, 7, 3, 15], 8) == [1, 7])
print(Solution().sum_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6])
print(Solution().sum_pairs([20, -13, 40], -7) == [])
print(Solution().sum_pairs([1, 2, 3, 4, 1, 0], 2) == [1, 1])
print(Solution().sum_pairs([4, -2, 3, 3, 4], 8) == [4, 4])
print(Solution().sum_pairs([0, 2, 0], 0) == [0, 0])
print(Solution().sum_pairs([5, 9, 13, -3], 10) == [13, -3])
