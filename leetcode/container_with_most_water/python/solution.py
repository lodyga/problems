class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        max_area = 0

        for i, h1 in enumerate(height[:-1]):
            for j, h2 in enumerate(height[i+1:]):
                area = min(h1, h2) * (j + 1)
                max_area = max(max_area, area)

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(Solution().maxArea([1, 1]) == 1)
print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) == 17)