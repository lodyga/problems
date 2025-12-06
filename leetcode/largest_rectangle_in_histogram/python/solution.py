class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        # stores monotonic increasing height tuples
        height_stack = []  # [(index, height), ]
        max_area = heights[0]

        for index, height in enumerate(heights):
            start = index
            while height_stack and height_stack[-1][1] > height:
                start, prev_height = height_stack.pop()
                max_area = max(
                    max_area, prev_height * (index - start)
                )
            height_stack.append((start, height))

        for index, height in height_stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area


class Solution2:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        max_area = 0

        for left in range(len(heights)):
            min_height = heights[left]
            
            for right in range(left, len(heights)):
                min_height = min(min_height, heights[right])
                area = min_height * (right - left + 1)
                max_area = max(max_area, area)
        
        return max_area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10)
print(Solution().largestRectangleArea([2, 4]) == 4)
print(Solution().largestRectangleArea([2, 1, 2]) == 3)
