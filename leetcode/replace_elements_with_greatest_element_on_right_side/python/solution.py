class Solution:
    def replaceElements(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        number_list = [-1]
        max_number = -1

        for number in reversed(numbers[1:]):
            max_number = max(max_number, number)
            number_list.append(max_number)

        number_list.reverse()
        return number_list


# O(n), O(n)
class Solution:
    def replaceElements(self, numbers: list[int]) -> list[int]:
        greatest_right = [-1] * len(numbers)

        for index, number in enumerate(numbers[::-1][:-1], 1):
            greatest_right[index] = max(number, greatest_right[index - 1])
        
        greatest_right.reverse()
        
        return greatest_right


# O(n), O(n)
class Solution:
    def replaceElements(self, numbers: list[int]) -> list[int]:
        numbers.pop(0)
        numbers.append(-1)

        for index in range(len(numbers) - 1)[::-1]:
            numbers[index] = max(numbers[index], numbers[index + 1])
        
        return numbers


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])
print(Solution().replaceElements([400]), [-1])