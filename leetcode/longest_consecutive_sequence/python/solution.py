class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash set
            A: iteration
        """
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            index = 0
            while num + index in num_set:
                index += 1
                max_length = max(max_length, index)
        
        return max_length


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
print(Solution().longestConsecutive([1, 0, 1, 2]) == 3)
print(Solution().longestConsecutive([]) == 0)
