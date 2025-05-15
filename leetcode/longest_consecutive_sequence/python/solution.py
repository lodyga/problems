class Solution:
    def longestConsecutive(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        number_set = set(numbers)
        longest_consec = 1

        for number in number_set:
            if number - 1 not in number_set:
                index = 1
                while number + index in number_set:
                    index += 1
                longest_consec = max(longest_consec, index)

        return longest_consec


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
print(Solution().longestConsecutive([1, 0, 1, 2]), 3)