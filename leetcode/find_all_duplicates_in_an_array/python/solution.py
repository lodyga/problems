class Solution:
    def findDuplicates(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: negative marking
        """
        twices = []
        for number in numbers:
            if numbers[abs(number) - 1] > 0:
                numbers[abs(number) - 1] *= -1
            else:
                twices.append(abs(number))
        return twices


class Solution:
    def findDuplicates(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: upper bound markning
        """
        mod = 10**5
        twices = []
        for number in numbers:
            if numbers[number % mod - 1] > mod:
                twices.append(number % mod)
            else:
                numbers[number % mod - 1] += mod
        return twices


class Solution:
    def findDuplicates(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        number_set = set()
        twices = []
        for number in numbers:
            if number in number_set:
                twices.append(number)
            else:
                number_set.add(number)
        return twices


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3])
print(Solution().findDuplicates([1, 1, 2]) == [1])
print(Solution().findDuplicates([1]) == [])