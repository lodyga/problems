class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = 0
        max_counter = 0

        for num in nums:
            if num:
                counter += 1
                max_counter = max(max_counter, counter)
            else:
                counter = 0

        return max_counter


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3)
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2)
print(Solution().findMaxConsecutiveOnes([1]) == 1)
print(Solution().findMaxConsecutiveOnes([0]) == 0)
