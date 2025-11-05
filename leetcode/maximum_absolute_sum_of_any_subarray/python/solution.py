class Solution:
    def maxAbsoluteSum(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy
        Kadane's Algorithm
        """
        # search for positive sums
        element = 0
        max_element = numbers[0]
        for number in numbers:
            element = element + number if element > 0 else number
            max_element = max(max_element, element)

        # search for negative sums
        element = 0
        min_element1 = numbers[0]
        for number in numbers:
            element = element + number if element < 0 else number
            min_element1 = min(min_element1, element)

        return max(max_element, abs(min_element1))


print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) == 5)
print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8)
print(Solution().maxAbsoluteSum([-1, 5]) == 5)
