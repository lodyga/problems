class Solution:
    def missingNumber(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        number_set = set(numbers)
        for number in range(len(numbers) + 1):
            if number not in number_set:
                return number

class Solution:
    def missingNumber(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        xor = 0
        for number in range(len(numbers) + 1):
            xor ^= number
        
        for number in numbers:
            xor ^= number
        
        return xor


class Solution:
    def missingNumber(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: math
        """
        # total = sum(number for number in range(len(numbers) + 1))
        total = int(len(numbers) * (len(numbers) + 1) / 2)
        return total - sum(numbers)


print(Solution().missingNumber([3, 0, 1]) == 2)
print(Solution().missingNumber([0, 1]) == 2)
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)