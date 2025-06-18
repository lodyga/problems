r"""
draft
3, 4, 0, 1, 2
4, 0, 1, 2, 3
0, 1, 2, 3, 4

2, 3, 4, 0, 1
1, 2, 3, 4, 0
"""


class Solution:
    def search(self, numbers: list[int], target: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 0
        right = len(numbers) - 1

        while left <= right:
            middle = (left + right) // 2
            middle_number = numbers[middle]

            if (
                middle_number == target or
                numbers[left] == target or
                numbers[right] == target
            ):
                return True
            elif middle_number < numbers[right]:
                if middle_number < target < numbers[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            elif numbers[left] < middle_number:
                if numbers[left] < target < middle_number:
                    right = middle - 1
                else:
                    left = middle + 1
            # No way to tell which side of portion is contiguous
            else:
                left += 1
                right -= 1

        return False


print(Solution().search([1, 2, 3, 4, 5], 2) == True)
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0) == True)
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3) == False)
print(Solution().search([1], 0) == False)
print(Solution().search([0, 1], 0) == True)
print(Solution().search([1, 0], 0) == True)
print(Solution().search([0, 1], 1) == True)
print(Solution().search([1, 0], 1) == True)
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) == True)
print(Solution().search([1, 0, 1, 1, 1], 0) == True)
print(Solution().search([1, 0, 0], 1) == True)