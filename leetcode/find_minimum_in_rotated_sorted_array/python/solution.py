# draft
# if middle < right: search left (or is min)

# 1, 2, 3, 4, 5
# 4, 5, 1, 2, 3
# 5, 1, 2, 3, 4

# 2, 3, 4, 5, 1
# 3, 4, 5, 1, 2


class Solution:
    def findMin(self, numbers: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = len(numbers) - 1
        min_number = numbers[0]

        while left <= right:
            # early exit
            if numbers[left] < numbers[right]:
                return min(min_number, numbers[left])

            middle = (left + right) // 2
            middle_number = numbers[middle]
            min_number = min(min_number, middle_number)

            if middle_number < numbers[right]:
                right = middle - 1
            else:
                left = middle + 1
            
        return min_number


class Solution:
    def findMin(self, numbers: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search (lower bound)
        """
        left = 0
        right = len(numbers) - 1
        min_number = numbers[0]

        while left <= right:
            middle = (left + right) // 2
            middle_number = numbers[middle]
            min_number = min(min_number, middle_number)

            if middle_number < numbers[right]:
                right = middle
            else:
                left = middle + 1
            
        return min_number


print(Solution().findMin([1, 2, 3, 4]) == 1)
print(Solution().findMin([4, 1, 2, 3]) == 1)
print(Solution().findMin([2, 3, 4, 1]) == 1)
print(Solution().findMin([3, 4, 1, 2]) == 1)
print(Solution().findMin([4, 5, 1, 2, 3]) == 1)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([1, 2, 3, 4, 5]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([1]) == 1)
print(Solution().findMin([3, 1, 2]) == 1)