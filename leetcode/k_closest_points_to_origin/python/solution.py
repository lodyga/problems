import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        distance_list = []
        heapq.heapify(distance_list)

        for x, y in points:
            distance = (x**2 + y**2) #** 0.5
            if len(distance_list) < k:
                heapq.heappush(distance_list, [-distance, x, y])
            else:
                heapq.heappushpop(distance_list, [-distance, x, y])
        
        return [[x, y] for _, x, y in distance_list]


print(Solution().kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[-2, 4], [3, 3]])
print(Solution().kClosest([[1, 3], [-2, 2], [2, -2]], 2), [[-2, 2], [2, -2]])