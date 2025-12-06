class Solution:
    def flood_depth(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: two pointers
        """
        left = 0
        right = len(heights) - 1
        max_left_height = heights[0]
        max_right_height = heights[right]
        max_depth = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            if left_height < right_height:
                max_left_height = max(max_left_height, left_height)
                depth = max_left_height - left_height
                left += 1
            else:
                max_right_height = max(max_right_height, right_height)
                depth = max_right_height - right_height
                right -= 1
            max_depth = max(max_depth, depth)

        return max_depth


print(Solution().flood_depth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) == 2)
print(Solution().flood_depth([5, 8]) == 0)
print(Solution().flood_depth([3, 1, 2]) == 1)
print(Solution().flood_depth([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 2)
