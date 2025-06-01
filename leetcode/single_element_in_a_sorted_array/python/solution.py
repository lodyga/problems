class Solution:
    def singleNonDuplicate(self, numbers: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            middle = (left + right) // 2
            middle_number = numbers[middle]
            is_portion_odd = (middle - left) % 2

            if numbers[middle - 1] != middle_number and numbers[middle + 1] != middle_number:
                return middle_number
            elif (is_portion_odd and numbers[middle - 1] == middle_number):
                left = middle + 1
            elif (is_portion_odd and numbers[middle + 1] == middle_number):
                right = middle - 1
            elif (not is_portion_odd and numbers[middle - 1] == middle_number):
                right = middle - 2
            elif (not is_portion_odd and numbers[middle + 1] == middle_number):
                left = middle + 2
        return numbers[left]


class Solution:
    def singleNonDuplicate(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: slick
        """
        xorr = 0
        for number in numbers:
            xorr ^= number
        return xorr


print(Solution().singleNonDuplicate([1]) == 1)
print(Solution().singleNonDuplicate([1, 2, 2]) == 1)
print(Solution().singleNonDuplicate([1, 1, 2]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) == 3)
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]) == 4)