class Solution:
    def sum_pairs(self, numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        unique_numbers = set()

        for number in numbers:
            complement = target - number
            if complement in unique_numbers:
                return [complement, number]
            else:
                unique_numbers.add(number)
        return None


print(Solution().sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7])
print(Solution().sum_pairs([1, 4, 8, 7, 3, 15], 8) == [1, 7])
print(Solution().sum_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6])
print(Solution().sum_pairs([20, -13, 40], -7) == None)
print(Solution().sum_pairs([1, 2, 3, 4, 1, 0], 2) == [1, 1])
print(Solution().sum_pairs([4, -2, 3, 3, 4], 8) == [4, 4])
print(Solution().sum_pairs([0, 2, 0], 0) == [0, 0])
print(Solution().sum_pairs([5, 9, 13, -3], 10) == [13, -3])
