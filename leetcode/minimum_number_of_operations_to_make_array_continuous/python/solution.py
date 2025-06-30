class Solution:
    def minOperations(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        unique_numbers = sorted(set(numbers))
        min_operations = len(numbers) - 1
        right = 0

        for left, number in enumerate(unique_numbers):
            while (
                right < len(unique_numbers) and
                unique_numbers[right] < number + len(numbers)
            ):
                right += 1

            window_length = right - left
            operations = len(numbers) - window_length
            min_operations = min(min_operations, operations)

        return min_operations


class Solution:
    def minOperations(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        number_set = set(numbers)
        numbers.sort()
        min_operations = len(numbers) - 1

        for number in number_set:
            operations = 0
            
            for index in range(1, len(numbers)):
                operations += number + index not in number_set
            
            min_operations = min(min_operations, operations)
        
        return min_operations


print(Solution().minOperations([2, 3, 5, 9]) == 1)
print(Solution().minOperations([4, 2, 5, 3]) == 0)
print(Solution().minOperations([1, 2, 3, 5, 6]) == 1)
print(Solution().minOperations([1, 10, 100, 1000]) == 3)
print(Solution().minOperations([8, 5, 9, 9, 8, 4]) == 2)
print(Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) == 6)