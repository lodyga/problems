class NumArray:
    """
    Time complexity: 
        constructor: O(n)
        sumRange: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list
        A: prefix sum
    """

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5))  # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5))  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
