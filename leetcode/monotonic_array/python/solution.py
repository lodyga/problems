class Solution:
    def isMonotonic(self, numbers) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        def is_increasing():
            for index in range(len(numbers) - 1):
                if numbers[index + 1] < numbers[index]:
                    return False
            return True

        def is_decreasing():
            for index in range(len(numbers) - 1):
                if numbers[index + 1] > numbers[index]:
                    return False
            return True

        return is_increasing() or is_decreasing()


print(Solution().isMonotonic([1, 2, 2, 3]), True)
print(Solution().isMonotonic([6, 5, 4, 4]), True)
print(Solution().isMonotonic([1, 3, 2]), False)