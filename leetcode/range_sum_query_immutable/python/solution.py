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
        self.prefixes = [0] * (len(numbers) + 1)
        for index in range(len(numbers)):
            self.prefixes[index + 1] = self.prefixes[index] + numbers[index]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right + 1] - self.prefixes[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5))  # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5))  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3