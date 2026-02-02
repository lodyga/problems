class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: sorting
        """
        x_points = sorted(x for x, _ in points)
        res = 0

        for index in range(len(x_points) - 1):
            x1 = x_points[index]
            x2 = x_points[index + 1]
            res = max(res, x2 - x1)

        return res


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, array
            A: sorting
        """
        x_points = set()

        for x, _ in points:
            x_points.add(x)

        x_points = sorted(x_points)
        res = 0

        for index in range(len(x_points) - 1):
            x1 = x_points[index]
            x2 = x_points[index + 1]
            res = max(res, x2 - x1)

        return res


print(Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) == 1)
print(Solution().maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3)
