class Solution:
    def trap(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0
        right = len(heights) - 1
        max_left_height = heights[left]
        max_right_height = heights[right]
        trapped_water = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            if left_height < right_height:
                max_left_height = max(max_left_height, left_height)
                trapped_water += max_left_height - left_height
                left += 1
            else:
                max_right_height = max(max_right_height, right_height)
                trapped_water += max_right_height - right_height
                right -= 1

        return trapped_water


print(Solution().trap([3, 1, 2]) == 1)
print(Solution().trap([5, 8]) == 0)
print(Solution().trap([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) == 8)
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
print(Solution().trap([4, 2, 0, 3, 2, 5]) == 9)