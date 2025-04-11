class Solution:
    def containsDuplicate(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        unique_numbers = set()
        for number in numbers:
            if number in unique_numbers:
                return True
            else:
                unique_numbers.add(number)
        return False


class Solution:
    def containsDuplicate(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: One-liner
        """
        return len(numbers) != len(set(numbers))


print(Solution().containsDuplicate([1, 2, 3]) == False)
print(Solution().containsDuplicate([1, 2, 3, 4]) == False)
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
