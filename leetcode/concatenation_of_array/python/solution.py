class Solution:
    def getConcatenation(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        concatenated_list = [None] * len(numbers) * 2
        
        for index, number in enumerate(numbers):
            concatenated_list[index] = number
            concatenated_list[index + len(numbers)] = number
        
        return concatenated_list


class Solution:
    def getConcatenation(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        numbers.extend(numbers)
        return numbers


class Solution:
    def getConcatenation(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        numbers = numbers + numbers
        return numbers


print(Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1])
print(Solution().getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1])