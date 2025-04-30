class Solution:
    def searchInsert(self, numbers: list[int], target: int) -> int:
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

            if target == middle_number:
                return middle
            elif target < middle_number:
                right = middle - 1
            else:
                left = middle + 1
        
        return left


print(Solution().searchInsert([1, 3, 5, 6], 1) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 3) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 5) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 6) == 3)
print(Solution().searchInsert([1, 3, 5, 6], 0) == 0)
print(Solution().searchInsert([1, 3, 5, 6], 2) == 1)
print(Solution().searchInsert([1, 3, 5, 6], 4) == 2)
print(Solution().searchInsert([1, 3, 5, 6], 7) == 4)