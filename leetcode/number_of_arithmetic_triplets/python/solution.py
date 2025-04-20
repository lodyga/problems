class Solution:
    def arithmeticTriplets(self, numbers: list[int], delta: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        unique_numbers = set(numbers)
        counter = 0

        for number in unique_numbers:
            if (number + delta in unique_numbers and
                    number + 2*delta in unique_numbers):
                counter += 1

        return counter


print(Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2)
print(Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2)
