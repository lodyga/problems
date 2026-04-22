class Solution:
    def arraySign(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        is_positive = True

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                is_positive = not is_positive
        
        return 1 if is_positive else -1


print(Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1)
print(Solution().arraySign([1, 5, 0, 2, -3]) == 0)
print(Solution().arraySign([-1, 1, -1, 1, -1]) == -1)
