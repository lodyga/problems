class Solution:
    def findDisappearedNumbers(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        number_set = set(numbers)
        return [number
                for number in range(1, len(numbers) + 1)
                if number not in number_set]


class Solution:
    def findDisappearedNumbers(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        number_range = set(range(1, len(numbers) + 1))

        for number in numbers:
            number_range.discard(number)

        return list(number_range)


class Solution:
    def findDisappearedNumbers(self, numbers: list[int]) -> list[int]:
        for number in numbers:
            numbers[abs(number) - 1] = -abs(numbers[abs(number) - 1])

        return [index for
                index, number in enumerate(numbers, 1)
                if number > 0]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
print(Solution().findDisappearedNumbers([1, 1]), [2])
