class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        points.sort()
        arrow_counter = 0

        index = 0
        while index < len(points):
            _, earliest_end = points[index]
            arrow_counter += 1
            index += 1
            while (
                index < len(points) and 
                points[index][0] <= earliest_end
            ):
                _, end = points[index]
                earliest_end = min(earliest_end, end)
                index += 1

        return arrow_counter


import heapq


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        heapq.heapify(points)
        arrow_counter = 0
        earliest_end = 0

        while points:
            _, earliest_end = heapq.heappop(points)
            arrow_counter += 1
            while points and points[0][0] <= earliest_end:
                _, end = heapq.heappop(points)
                earliest_end = min(earliest_end, end)

        return arrow_counter


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2)
print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4)
print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2)
print(Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]) == 2)
print(Solution().findMinArrowShots([[-2147483648, 2147483647]]) == 1)