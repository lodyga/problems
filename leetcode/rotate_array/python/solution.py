"""
draft
[1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
[5, 4, 3, 2, 1]  # reverse numbers
[4, 5, 1, 2, 3]  # reverse before and after pivot
"""


class Solution:
    def rotate(self, numbers: list[int], k: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        slick
        """
        k %= len(numbers)

        def reverse_inplace(left, right):
            while left < right:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
                right -= 1

        reverse_inplace(0, len(numbers) - 1)
        reverse_inplace(0, k - 1)
        reverse_inplace(k, len(numbers) - 1)

        return numbers


class Solution:
    def rotate(self, numbers: list[int], k: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: build-in function
        """
        pivot = len(numbers) - k % len(numbers)
        return numbers[pivot:] + numbers[: pivot]


class Solution:
    def rotate(self, numbers: list[int], k: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: iteration
        """
        k %= len(numbers)
        numbers_copy = [0] * len(numbers)

        for left in range(len(numbers)):
            right = (left + k) % len(numbers)
            numbers_copy[right] = numbers[left]

        numbers[:] = numbers_copy
        return numbers


print(Solution().rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
print(Solution().rotate([1, 2, 3], 2) == [2, 3, 1])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([1, 2, 3, 4, 5, 6], 1) == [6, 1, 2, 3, 4, 5])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100])
print(Solution().rotate([-1], 2) == [-1])
print(Solution().rotate([1, 2], 3) == [2, 1])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38) == [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])