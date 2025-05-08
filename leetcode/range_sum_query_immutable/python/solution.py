from typing import List


class NumArray:
    """
    Time complexity: 
        constructor: O(n)
        sumRange: O(1)
    Auxiliary space complexity: O(n)
    Tags: prefix sum
    """

    def __init__(self, numbers: List[int]):
        self.values = [0] * (len(numbers) + 1)
        for index, number in enumerate(numbers, 1):
            self.values[index] = self.values[index - 1] + number

    def sumRange(self, left: int, right: int) -> int:
        return self.values[right + 1] - self.values[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5))  # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5))  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3