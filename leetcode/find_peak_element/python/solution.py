class Solution:
    def findPeakElement(self, numbers: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = len(numbers) - 1

        while left <= right:
            middle = (left + right) // 2
            middle_number = numbers[middle]
            prev_number = middle_number - 1 if middle == 0 else numbers[middle - 1]
            next_number = middle_number - 1 if middle == len(numbers) - 1 else numbers[middle + 1]

            if (
                prev_number < middle_number and
                middle_number > next_number
            ):
                return middle
            elif (
                middle != len(numbers) - 1 and
                middle_number < numbers[middle + 1]
            ):
                left = middle + 1
            else:
                right = middle - 1


print(Solution().findPeakElement([1, 2, 3, 1]) == 2)
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
print(Solution().findPeakElement([1]) == 0)
print(Solution().findPeakElement([1, 2]) == 1)