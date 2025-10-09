class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        numbers.sort()
        max_number = 1
        for index in range(1, len(numbers)):
            if numbers[index] > max_number:
                max_number += 1
        return max_number


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy
        """
        n = len(arr)
        count = [0] * (n + 1)

        for num in arr:
            count[min(num, n)] += 1

        prev = 1
        for num in range(2, n + 1):
            prev = min(prev + count[num], num)

        return prev


print(Solution().maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2)
print(Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3)
print(Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5)
print(Solution().maximumElementAfterDecrementingAndRearranging([73, 98, 9]) == 3)
print(Solution().maximumElementAfterDecrementingAndRearranging([5, 3, 3, 1]) == 4)