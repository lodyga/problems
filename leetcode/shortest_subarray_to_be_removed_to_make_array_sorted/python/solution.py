class Solution:
    def findLengthOfShortestSubarray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        # Find longest non-decreasing prefix
        left = 0
        while (
            left + 1 < len(numbers) and
            numbers[left] <= numbers[left + 1]
        ):
            left += 1
        if left == len(numbers) - 1:
            return 0
            
        # Find longest non-decreasing suffix
        right = len(numbers) - 1
        while (
            right > 0 and
            numbers[right - 1] <= numbers[right]
        ):
            right -= 1

        result = min(len(numbers) - (left + 1), right)

        # # Try to merge prefix with suffix
        i = 0
        j = right
        while (
            i <= left and
            j < len(numbers)
        ):
            if numbers[i] <= numbers[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result


print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3)
print(Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4)
print(Solution().findLengthOfShortestSubarray([1, 2, 3]) == 0)
print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 0, 7, 8, 9]) == 2)