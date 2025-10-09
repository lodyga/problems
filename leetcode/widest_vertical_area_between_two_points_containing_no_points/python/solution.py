class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        xes = set()
        
        for x, _ in points:
            xes.add(x)
        
        xes = sorted(xes)
        max_x = 0
        
        for index in range(len(xes) - 1):
            max_x = max(max_x, xes[index + 1] - xes[index])

        return max_x


print(Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) == 1)
print(Solution().maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3)