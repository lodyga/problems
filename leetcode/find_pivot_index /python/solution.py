class Solution:
    def pivotIndex(self, numbers: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: prefix sum
        """
        prefix_sum = 0
        postfix_sum = sum(numbers)
        for index in range(len(numbers)):
            postfix_sum -= numbers[index]
            prefix_sum += numbers[index - 1] if index else 0

            if prefix_sum == postfix_sum:
                return index
        
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]), 3)
print(Solution().pivotIndex([1, 2, 3]), -1)
print(Solution().pivotIndex([2, 1, -1]), 0)