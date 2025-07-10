class MountainArray:
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def get(self, index: int) -> int:
        return self.numbers[index]

    def length(self) -> int:
        return len(self.numbers)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        length = mountainArr.length()
        left = 1
        right = length - 2

        # find the mountain peak
        while left <= right:
            middle = (left + right) // 2
            middle_number = mountainArr.get(middle)
            left_number = mountainArr.get(middle - 1)
            right_number = mountainArr.get(middle + 1)

            if left_number < middle_number < right_number:
                left = middle + 1
            elif left_number > middle_number > right_number:
                right = middle - 1
            else:
                peak = middle
                break

        # search the left portion
        left = 0
        right = peak
        while left <= right:
            middle = (left + right) // 2
            middle_number = mountainArr.get(middle)
            if target == middle_number:
                return middle
            elif target < middle_number:
                right = middle - 1
            else:
                left = middle + 1

        # search the right portion
        left = peak + 1
        right = length - 1
        while left <= right:
            middle = (left + right) // 2
            middle_number = mountainArr.get(middle)
            if target == middle_number:
                return middle
            elif target > middle_number:
                right = middle - 1
            else:
                left = middle + 1

        return -1


print(Solution().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2)
print(Solution().findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])) == -1)