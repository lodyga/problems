class Solution:
    def trap(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        left = 0
        right = len(heights) - 1
        left_max = 0
        right_max = 0
        res = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            if left_height < right_height:
                left_max = max(left_max, left_height)
                res += left_max - left_height
                left += 1
            else:
                right_max = max(right_max, right_height)
                res += right_max - right_height
                right -= 1

        return res


print(Solution().trap([3, 1, 2]) == 1)
print(Solution().trap([5, 8]) == 0)
print(Solution().trap([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) == 8)
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
print(Solution().trap([4, 2, 0, 3, 2, 5]) == 9)
