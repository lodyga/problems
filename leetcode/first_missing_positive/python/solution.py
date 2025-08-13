import heapq


class Solution:
    def firstMissingPositive(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        numbers = [number for number in numbers if number > 0]
        heapq.heapify(numbers)
        
        number = 1
        while numbers and numbers[0] == number:
            heapq.heappop(numbers)
            number += 1
        
        return number


class Solution:
    def firstMissingPositive(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: negative marking
        """
        for index in range(len(numbers)):
            if numbers[index] < 0:
                numbers[index] = 0
        
        for index in range(len(numbers)):
            number = abs(numbers[index])
            if 0 < number <= len(numbers):
                if numbers[number - 1] == 0:
                    numbers[number - 1] = -(len(numbers) + 1)
                elif numbers[number - 1] > 0:
                    numbers[number - 1] = -numbers[number - 1]
        
        for index in range(len(numbers)):
            if numbers[index] >= 0:
                return index + 1
        
        return len(numbers) + 1


print(Solution().firstMissingPositive([1, 2, 0]) == 3)
print(Solution().firstMissingPositive([3, 4, -1, 1]) == 2)
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1)