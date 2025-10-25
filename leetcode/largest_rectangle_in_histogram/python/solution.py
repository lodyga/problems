class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        monotonic increasing stack
        """
        stack = []  # [(index, height), ]
        area = 0

        for index, height in enumerate(heights):
            prev_index = index
            while stack and stack[-1][1] > height:
                prev_index, prev_height = stack.pop()
                area = max(area, prev_height * (index - prev_index))
            
            stack.append((prev_index, height))
        
        for index in reversed(range(len(stack))):
            prev_index, prev_height = stack[index]
            area = max(area, prev_height * (len(heights) - prev_index))

        return area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10)
print(Solution().largestRectangleArea([2, 4]) == 4)
print(Solution().largestRectangleArea([2, 1, 2]) == 3)


# O(n2), O(1)
# brute force
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0

        for left in range(len(heights)):
            min_height = heights[left]
            
            for right in range(left, len(heights)):
                min_height = min(min_height, heights[right])
                current_area = min_height * (right - left + 1)
                max_area = max(max_area, current_area)
        
        return max_area