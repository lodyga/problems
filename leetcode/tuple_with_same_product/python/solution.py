import math


class Solution:
    def tupleSameProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        failed
        """
        quad = []

        def dfs(index, m, d):
            if m == d == 2:
                return math.prod(quad) == 1
            elif m > 2 or d > 2 or index == len(numbers):
                return 0

            number = numbers[index]
            # take and multiply
            quad.append(number)
            memo = dfs(index + 1, m + 1, d)
            quad.pop()
            # take and divide
            quad.append(1/number)
            memo += dfs(index + 1, m, d + 1)
            quad.pop()
            # skip
            memo += dfs(index + 1, m, d)

            return memo

        return dfs(0, 0, 0) * 4


class Solution:
    def tupleSameProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: iteration, math
        """
        number_frequency = {}
        for index in range(len(numbers)):
            for i2 in range(index + 1, len(numbers)):
                number = numbers[index] * numbers[i2]
                number_frequency[number] = number_frequency.get(number, 0) + 1
        
        tuple_counter = 0
        for number, frequency in number_frequency.items():
            if frequency > 1:
                tuple_counter += frequency * (frequency - 1) // 2
        return tuple_counter * 8


print(Solution().tupleSameProduct([2, 3, 4, 6]) == 8)
print(Solution().tupleSameProduct([1, 2, 4, 5, 10]) == 16)
print(Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]) == 40)
print(Solution().tupleSameProduct([10, 5, 15, 8, 6, 12, 20, 4]) == 72)
print(Solution().tupleSameProduct([30, 28, 20, 6, 24, 3, 12, 14, 2, 1]) == 72)
