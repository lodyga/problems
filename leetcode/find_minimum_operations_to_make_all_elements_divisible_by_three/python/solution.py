class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = 0
        for num in nums:
            counter += 1 if num % 3 else 0
        return counter


print(Solution().minimumOperations([1, 2, 3, 4]) == 3)
print(Solution().minimumOperations([3, 6, 9]) == 0)
