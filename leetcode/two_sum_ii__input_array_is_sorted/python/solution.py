class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if target == two_sum:
                return [left + 1, right + 1]
            elif target < two_sum:
                right = right - 1
            else:
                left = left + 1


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        for index in range(len(numbers) - 1):
            complement = target - numbers[index]
            left = index + 1
            right = len(numbers) - 1

            while left <= right:
                middle = (left + right) // 2

                if complement == numbers[middle]:
                    return [index + 1, middle + 1]
                elif complement < numbers[middle]:
                    right = middle - 1
                else:
                    left = middle + 1


print(Solution().twoSum([2, 7, 11, 15], 9), [1, 2])
print(Solution().twoSum([2, 3, 4], 6), [1, 3])
print(Solution().twoSum([-1, 0], -1), [1, 2])