class Solution:
    def majorityElement(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        frequencies = {}
        most_frequent_numbers = []
        threshold = len(numbers) // 3

        for number in numbers:
            frequencies[number] = frequencies.get(number, 0) + 1
        
        for nubmer, frequency in frequencies.items():
            if frequency > threshold:
                most_frequent_numbers.append(nubmer)

        return most_frequent_numbers


class Solution:
    def majorityElement(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Boyer-Moore Voting Algorithm
        """
        frequencies = {}
        most_frequent_numbers = []
        threshold = len(numbers) // 3

        for number in numbers:
            frequencies[number] = frequencies.get(number, 0) + 1

            if len(frequencies) > 2:
                number_frequency_copy = {}
                for number, frequency in frequencies.items():
                    if frequency > 1:
                        number_frequency_copy[number] = frequency - 1
                frequencies = number_frequency_copy

        for number in frequencies:
            if numbers.count(number) > threshold:
                most_frequent_numbers.append(number)

        return most_frequent_numbers


print(Solution().majorityElement([3, 3, 4]), [3])
print(Solution().majorityElement([3, 2, 3]), [3])
print(Solution().majorityElement([1]), [1])
print(Solution().majorityElement([1, 2]), [1, 2])
print(Solution().majorityElement([3, 4, 5, 3, 4]), [3, 4])
print(Solution().majorityElement([2, 2]), [2])
print(Solution().majorityElement([3, 4, 5, 3]), [3])
print(Solution().majorityElement([3, 4, 5]), [])