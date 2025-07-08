class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: hash set
        """        
        unique_numbers = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                number = grid[row][col]
                if number in unique_numbers:
                    repeated = number
                unique_numbers.add(number)
        
        for number in range(1, len(grid)**2 + 1):
            if number not in unique_numbers:
                missing = number
                break

        return [repeated, missing]


print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4])
print(Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [9, 5])