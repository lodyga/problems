class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        # stores monotonic increasing (height, index) tuples
        # [(height, idx), ]
        stack = []
        res = heights[0]

        for idx, height in enumerate(heights):
            start_idx = idx

            while stack and stack[-1][0] >= height:
                prev_height, start_idx = stack.pop()
                width = idx - start_idx
                res = max(res, prev_height * width)

            stack.append((height, start_idx))

        for height, idx in stack:
            width = len(heights) - idx
            res = max(res, height * width)

        return res


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = 0

        for left in range(len(heights)):
            min_height = heights[left]
            
            for right in range(left, len(heights)):
                min_height = min(min_height, heights[right])
                area = min_height * (right - left + 1)
                res = max(res, area)
        
        return res


print(Solution().largestRectangleArea([5]) == 5)
print(Solution().largestRectangleArea([2, 4]) == 4)
print(Solution().largestRectangleArea([4, 2]) == 4)
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10)
print(Solution().largestRectangleArea([2, 1, 2]) == 3)
