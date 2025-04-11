class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        seen_numbers = {}
        for index, number in enumerate(numbers):
            complement = target - number
            if complement in seen_numbers:
                return [seen_numbers[complement], index]
            else:
                seen_numbers[number] = index
        return None


print(Solution().twoSum([2, 7, 11, 15], 9) == [0, 1])
print(Solution().twoSum([3, 2, 4], 6) == [1, 2])
print(Solution().twoSum([3, 3], 6) == [0, 1])
print(Solution().twoSum([3, 3], 7) == None)
