class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: greedy, sorting
        """
        points.sort()
        res = 1
        prev_end = points[0][1]

        for (start, end) in points:
            if start <= prev_end:
                prev_end = min(end, prev_end)
                continue

            res += 1
            prev_end = end

        return res


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: greedy, sorting
        """
        points.sort(key=lambda point: point[1])
        res = 1
        prev_end = points[0][1]

d        for (start, end) in points:
            if start <= prev_end:
                continue

            res += 1
            prev_end = end

        return res


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2)
print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4)
print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2)
print(Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]) == 2)
print(Solution().findMinArrowShots([[-2147483648, 2147483647]]) == 1)
