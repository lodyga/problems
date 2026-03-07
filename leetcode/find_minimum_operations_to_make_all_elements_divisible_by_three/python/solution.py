class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        return sum(1 for num in nums if num % 3 != 0)


print(Solution().minimumOperations([1, 2, 3, 4]) == 3)
print(Solution().minimumOperations([3, 6, 9]) == 0)
