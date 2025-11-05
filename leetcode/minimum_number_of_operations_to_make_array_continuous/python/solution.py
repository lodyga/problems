class Solution:
    def minOperations(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        min_operations = len(numbers) - 1
        unique_sorted_numbers = sorted(set(numbers))
        right = 0

        for left, left_number in enumerate(unique_sorted_numbers):
            while (
                right < len(unique_sorted_numbers) and
                left_number + len(numbers) > unique_sorted_numbers[right]
            ):
                right += 1

            window = right - left
            operations = len(numbers) - window
            min_operations = min(min_operations, operations)

        return min_operations

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

            for diff in range(1, len(numbers)):
                if number + diff not in number_set:
                    operations += 1

            min_operations = min(min_operations, operations)
            if min_operations == 0:
                return 0

        return min_operations


print(Solution().minOperations([2, 3, 5, 9]) == 1)
print(Solution().minOperations([4, 2, 5, 3]) == 0)
print(Solution().minOperations([1, 2, 3, 5, 6]) == 1)
print(Solution().minOperations([1, 10, 100, 1000]) == 3)
print(Solution().minOperations([1, 9, 10, 11, 19]) == 2)
print(Solution().minOperations([1, 3, 5, 7, 9]) == 2)
print(Solution().minOperations([8, 5, 9, 9, 8, 4]) == 2)
print(Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) == 6)
