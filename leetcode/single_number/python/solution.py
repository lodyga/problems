class Solution:
    def singleNumber(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        xor = 0
        for number in numbers:
            xor ^= number
        return xor


class Solution:
    def singleNumber(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        unique_numbers = set()

        for number in numbers:
            if number in unique_numbers:
                unique_numbers.remove(number)
            else:
                unique_numbers.add(number)
        return unique_numbers.pop()


print(Solution().singleNumber([2, 2, 1]) == 1)
print(Solution().singleNumber([4, 1, 2, 1, 2]) == 4)
print(Solution().singleNumber([1]) == 1)