class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        res = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            
            height = min(left_height, right_height)
            width = right - left
            res = max(res, height * width)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return res


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = 0

        for i, h1 in enumerate(height[: -1]):
            for j, h2 in enumerate(height[i+1:]):
                area = min(h1, h2) * (j + 1)
                res = max(res, area)

        return res


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(Solution().maxArea([1, 1]) == 1)
print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) == 17)
