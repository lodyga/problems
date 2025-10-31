class Solution:
    def findErrorNums(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation, negative marking
        """
        for number in numbers:
            number = abs(number)
            if numbers[number - 1]  < 0:
                duplicate = number
                break
            else:
                numbers[number - 1] *= - 1

        xor = 0
        for index, number in enumerate(numbers, 1):
            xor ^= abs(number) ^ index
        missing = xor ^ duplicate

        return [duplicate, missing]


class Solution:
    def findErrorNums(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        number_set = set()
        for number in numbers:
            if number in number_set:
                duplicate = number
            else:
                number_set.add(number)

        for number in range(1, len(numbers) + 1):
            if number not in number_set:
                missing = number
                break

        return [duplicate, missing]


class Solution:
    def findErrorNums(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        number_frequency = {number: 0
                            for number in range(1, len(numbers) + 1)}
        
        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1
        
        duplicate = missing = 0
        for number, frequency in number_frequency.items():
            if frequency == 2:
                duplicate = number
                if missing:
                    break
            elif frequency == 0:
                missing = number
                if duplicate:
                    break

        return [duplicate, missing]


print(Solution().findErrorNums([1, 2, 2, 4]) == [2, 3])
print(Solution().findErrorNums([1, 1]) == [1, 2])
print(Solution().findErrorNums([2, 2]) == [2, 1])
print(Solution().findErrorNums([2, 3, 2]) == [2, 1])