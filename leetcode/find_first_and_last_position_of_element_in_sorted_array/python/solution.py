class Solution:
    def searchRange(self, numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = len(numbers) - 1
        lower_bound = -1

        while left <= right:
            middle = (left + right) // 2
            middle_number = numbers[middle]

            if middle_number == target:
                lower_bound = middle
                right = middle - 1
            elif middle_number > target:
                right = middle - 1
            else:
                left = middle + 1
            
        left = 0
        right = len(numbers) - 1
        upper_bound = -1
        while left <= right:
            middle = (left + right) // 2
            middle_number = numbers[middle]

            if middle_number == target:
                upper_bound = middle
                left = middle + 1
            elif middle_number < target:
                left = middle + 1
            else:
                right = middle - 1

        return [lower_bound, upper_bound]


print(Solution().searchRange([5, 5, 7], 5) == [0, 1])
print(Solution().searchRange([5, 7, 7], 7) == [1, 2])
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
print(Solution().searchRange([], 0) == [-1, -1])
print(Solution().searchRange([1], 1) == [0, 0])