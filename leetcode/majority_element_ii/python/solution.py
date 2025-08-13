class Solution:
    def majorityElement(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        number_frequency = {}
        most_frequent_numbers = []
        threshold = len(numbers) // 3

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1
        
        for nubmer, frequency in number_frequency.items():
            if frequency > threshold:
                most_frequent_numbers.append(nubmer)

        return most_frequent_numbers


class Solution:
    def majorityElement(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash map
        """
        number_frequency = {}
        most_frequent_numbers = []
        threshold = len(numbers) // 3

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1
            if len(number_frequency) > 2:
                number_frequency_copy = {}
                for number, frequency in number_frequency.items():
                    if frequency > 1:
                        number_frequency_copy[number] = frequency - 1
                number_frequency = number_frequency_copy

        for number in number_frequency:
            if numbers.count(number) > threshold:
                most_frequent_numbers.append(number)

        return most_frequent_numbers


print(Solution().majorityElement([3, 2, 3]), [3])
print(Solution().majorityElement([1]), [1])
print(Solution().majorityElement([1, 2]), [1, 2])
print(Solution().majorityElement([3, 4, 5, 3, 4]), [3, 4])