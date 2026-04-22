class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up
        """
        res = nums[0]
        max_total = 1
        min_total = 1

        for num in nums:
            min_total, _, max_total = sorted(
                (num, min_total * num, max_total * num))
            res = max(res, max_total)

        return res


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        N = len(nums)
        res = nums[0]

        for left in range(N):
            total = 1

            for right in range(left + 1, N):
                total *= nums[right]
                res = max(res, total)

        return res


print(Solution().maxProduct([-2]) == -2)
print(Solution().maxProduct([-4, -3]) == 12)
print(Solution().maxProduct([2, 3, -2, 4]) == 6)
print(Solution().maxProduct([-2, 0, -1]) == 0)
print(Solution().maxProduct([-2, -3, 7]) == 42)
print(Solution().maxProduct([2, -5, -2, -4, 3]) == 24)
print(Solution().maxProduct([0]) == 0)
print(Solution().maxProduct([-2, 0]) == 0)
print(Solution().maxProduct([0, 2]) == 2)
