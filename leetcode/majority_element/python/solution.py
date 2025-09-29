class Solution:
    def majorityElement(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        Boyer-Moore Voting Algorithm
        """
        counter = 0
        
        for number in numbers:
            if counter == 0:
                major = number
                counter = 1
            else:
                counter += 1 if major == number else - 1

        return major


class Solution:
    def majorityElement(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        number_frequency = {}
        most_frequent_number = None
        most_frequency = 0

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1
            if (number_frequency[number] > most_frequency):
                most_frequent_number = number
                most_frequency = number_frequency[number]

        return most_frequent_number


print(Solution().majorityElement([3, 2, 3]), 3)
print(Solution().majorityElement([3, 3, 4]), 3)
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)