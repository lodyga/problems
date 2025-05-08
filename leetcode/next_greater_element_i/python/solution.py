from typing import List


class Solution:
    def nextGreaterElement(self, numbers_1: List[int], numbers_2: List[int]) -> List[int]:
        """
        Time complexity: O(n)
            m: numbers_1 length
            n: numbers_2 length (n >= m)
        Auxiliary space complexity: O(n)
        Tags: stack, monotonic stack, monotonically decreasing stack
        """
        next_greater = [-1] * len(numbers_2)
        stack = []
        numbers_2_map = {number: index
                         for index, number
                         in enumerate(numbers_2)}

        # find next greter elements in numebrs_2
        for index, number in enumerate(numbers_2):
            while stack and number > stack[-1]:
                prev_number = stack.pop()
                next_greater[numbers_2_map[prev_number]] = number
            stack.append(number)

        # map next greater elements from numbers_2 to numbers_1 order
        next_greater_map = []
        for number in numbers_1:
            index = numbers_2_map[number]
            next_greater_map.append(next_greater[index])

        return next_greater_map


class Solution:
    def nextGreaterElement(self, numbers_1: List[int], numbers_2: List[int]) -> List[int]:
        """
        Time complexity: O(m*n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        next_greater = [-1] * len(numbers_2)
        numbers_2_map = {number: index
                         for index, number
                         in enumerate(numbers_2)}

        # find next greter elements in numebrs_2
        for index, number in enumerate(numbers_2[:-1]):
            for number_2 in numbers_2[index + 1:]:
                if number_2 > number:
                    next_greater[index] = number_2
                    break

        # map next greater elements from numbers_2 to numbers_1 order
        next_greater_map = []
        for number in numbers_1:
            index = numbers_2_map[number]
            next_greater_map.append(next_greater[index])

        return next_greater_map


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])
print(Solution().nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]), [7, 7, 7, 7, 7])