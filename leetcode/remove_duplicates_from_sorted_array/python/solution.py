class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0

        for right in range(len(numbers)):
            if numbers[left] == numbers[right]:
                continue
            else:
                left += 1
                numbers[left] = numbers[right]
        
        return left + 1


print(Solution().removeDuplicates([1, 1, 2]), 2)
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)