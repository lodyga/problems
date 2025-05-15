# prefix product
# [1, 2, 6, 24]
# postfix product
# [60, 20, 5, 1]


class Solution:
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        prefix = [1] * len(numbers)
        for index, number in enumerate(numbers[:-1]):
            prefix[index + 1] = prefix[index] * number

        postfix = [1] * len(numbers)
        for index in reversed(range(1, len(numbers))):
            postfix[index - 1] = postfix[index] * numbers[index]

        return [prefix[index] * postfix[index]
                for index in range(len(numbers))]


class Solution:
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: prefix sum
        """
        product = [1] * len(numbers)
        for index, number in enumerate(numbers[:-1]):
            product[index + 1] = product[index] * number

        postfix = 1
        for index in reversed(range(len(numbers))):
            product[index] *= postfix
            postfix *= numbers[index]

        return product


print(Solution().productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24])
print(Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])