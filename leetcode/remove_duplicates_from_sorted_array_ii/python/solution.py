class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 1

        for right in range(2, len(numbers)):
            # if numbers[left - 1] == numbers[left] == numbers[right]:
            if numbers[left - 1] == numbers[right]:
                continue
            else:
                left += 1
                numbers[left] = numbers[right]

        return left + 1


class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 1

        for right in range(2, len(numbers)):
            if numbers[left - 1] < numbers[right]:
                left += 1
                numbers[left] = numbers[right]

        return left + 1


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5)
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7)