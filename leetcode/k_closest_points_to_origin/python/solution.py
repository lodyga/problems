import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap
            A: heap
        """
        point_heap = []

        for x, y in points:
            dist = x**2 + y**2

            if len(point_heap) < k:
                heapq.heappush(point_heap, (-dist, x, y))
            else:
                heapq.heappushpop(point_heap, (-dist, x, y))

        return [[x, y] for _, x, y in point_heap]


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(k)
        Tags:
            A: sorting, build-in function
        """
        points.sort(key=lambda x: (x[0]**2 + x[1]**2))
        return points[: k]


print(sorted(Solution().kClosest([[1, 3], [-2, 2]], 1)) == sorted([[-2, 2]]))
print(sorted(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == sorted([[-2, 4], [3, 3]]))
print(sorted(Solution().kClosest([[1, 3], [-2, 2], [2, -2]], 2)) == sorted([[-2, 2], [2, -2]]))
