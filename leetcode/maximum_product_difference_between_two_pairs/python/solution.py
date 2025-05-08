class Solution:
    def maxProductDifference(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        min_number = almost_min_number = max_number = almost_max_number = numbers[0]

        for number in numbers:
            if number > max_number:
                max_number, almost_max_number = number, max_number
            elif number > almost_max_number:
                almost_max_number = number
            elif number < min_number:
                min_number, almost_min_number = number, min_number
            elif number < almost_min_number:
                almost_min_number = number

        return max_number * almost_max_number - min_number * almost_min_number


print(Solution().maxProductDifference([5, 6, 2, 7, 4]), 34)
print(Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]), 64)
