class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up (Kadane)
        """
        max_product = nums[0]
        min_total = 1
        max_total = 1

        for num in nums:
            triplet = (min_total * num, max_total * num, num)
            min_total = min(triplet)
            max_total = max(triplet)
            max_product = max(max_product, max_total)

        return max_product


class Solution2:
    def maxProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        max_product = numbers[0]

        for left in range(len(numbers)):
            val = 1
            for right in range(left + 1, len(numbers)):
                val *= numbers[right]
                max_product = max(max_product, val)

        return max_product



print(Solution().maxProduct([-2]) == -2)
print(Solution().maxProduct([-4, -3]) == 12)
print(Solution().maxProduct([2, 3, -2, 4]) == 6)
print(Solution().maxProduct([-2, 0, -1]) == 0)
print(Solution().maxProduct([-2, -3, 7]) == 42)
print(Solution().maxProduct([2, -5, -2, -4, 3]) == 24)
print(Solution().maxProduct([0]) == 0)
print(Solution().maxProduct([-2, 0]) == 0)
print(Solution().maxProduct([0, 2]) == 2)
