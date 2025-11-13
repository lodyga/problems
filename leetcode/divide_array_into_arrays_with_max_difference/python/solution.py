class Solution:
    def divideArray(self, numbers: list[int], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        numbers.sort()
        matrix = [[0] * 3 for _ in range(len(numbers) // 3)]

        for index, number in enumerate(numbers):
            row = index // 3
            col = index % 3
            matrix[row][col] = number
            if col and number - matrix[row][0] > k:
                return []
        
        return matrix


class Solution:
    def divideArray(self, numbers: list[int], k: int) -> list[list[int]]:
        """
        Time complexity: O(n)
            O(10**5)
        Auxiliary space complexity: O(n)
        Tags: counting sort
        """
        matrix = [[0] * 3 for _ in range(len(numbers) // 3)]
        number_frequency = [0] * (10**5 + 1)

        for number in numbers:
            number_frequency[number] += 1
        
        row = 0
        col = 0
        for number, frequency in enumerate(number_frequency):
            if frequency == 0:
                continue    
            
            while frequency:
                matrix[row][col] = number
                col += 1
                if col == 3:
                    if matrix[row][col - 1] - matrix[row][0] > k:
                        return []
                    col = 0
                    row += 1
                frequency -= 1
        
        return matrix


class Solution:
    def divideArray(self, numbers: list[int], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        numbers.sort()
        matrix = []

        for index in range(0, len(numbers), 3):
            if numbers[index + 2] - numbers[index] > k:
                return []
            
            matrix.append(numbers[index: index + 3])

        return matrix


print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]])
print(Solution().divideArray([2, 4, 2, 2, 5, 2], 2) == [])
print(Solution().divideArray([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14) == [[2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]])
