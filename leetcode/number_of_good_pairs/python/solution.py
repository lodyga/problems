class Solution:
    def numIdenticalPairs(self, numbers: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: math
        """
        number_frequency = {}
        pair_counter = 0

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        for frequency in number_frequency.values():
            # n! / ((n-2)! * 2) === n * (n - 1) / 2
            pair_counter += frequency * (frequency - 1) // 2
        return pair_counter


class Solution:
    def numIdenticalPairs(self, numbers: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: math
        """
        def factorial(number):
            if number == 0:
                return 1
            return number * factorial(number - 1)

        number_frequency = {}
        pair_counter = 0

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        for frequency in number_frequency.values():
            if frequency > 1:
                pair_counter += (
                    factorial(frequency) //
                    (factorial(frequency - 2) * 2))
        return pair_counter


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)
print(Solution().numIdenticalPairs([1, 1, 1, 1]), 6)
print(Solution().numIdenticalPairs([1, 2, 3]), 0)