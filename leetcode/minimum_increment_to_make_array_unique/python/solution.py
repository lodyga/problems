class Solution:
    def minIncrementForUnique(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting, two pointers
        """
        numbers.sort()
        counter = 0

        for index in range(1, len(numbers)):
            number = numbers[index]
            
            if numbers[index - 1] < number:
                continue
            
            numbers[index] = numbers[index - 1] + 1
            counter += numbers[index] - number

        return counter


class Solution:
    def minIncrementForUnique(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: counting sort
        """
        counter = 0
        frequency = {}
        
        for number in numbers:
            frequency[number] = frequency.get(number, 0) + 1

        max_number = max(numbers)
        number = min(numbers)
        while (
            number <= max_number or 
            number in frequency
        ):
            if number in frequency:
                diff = frequency[number] - 1
                if diff:
                    frequency[number + 1] = frequency.get(number + 1, 0) + diff
                    counter += diff

            number += 1

        return counter


class Solution:
    def minIncrementForUnique(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        length = 10**5 + 1
        frequency = [0] * length
        
        for number in numbers:
            frequency[number] += 1
        
        # counter = 0
        # for index in range(length):
        #     counter += frequency[index]
        #     if counter == len(numbers):
        #         frequency = frequency[:index + 1]
        #         break

        max_value = 0
        carry = []
        
        for number in frequency:
            if number == 0:
                if not carry:
                    continue
                
                max_value += carry.pop()
                for index in range(len(carry)):
                    carry[index] += 1
            else:
                for index in range(len(carry)):
                    carry[index] += 1
                for _ in range(number - 1):
                    carry.append(1)
            
        return max_value


print(Solution().minIncrementForUnique([1, 2, 2]) == 1)
print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6)
print(Solution().minIncrementForUnique([2, 2, 2, 1]) == 3)
print(Solution().minIncrementForUnique([1, 3, 0, 3, 0]) == 3)