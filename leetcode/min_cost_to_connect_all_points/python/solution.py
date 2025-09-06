import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: MSP
        Minimum Spanning Tree, Prim's alg
        """
        adjs = {point: set() for point in range(len(points))}  # {point: (distance, adj_point)}
        for i in range(len(points)):
            xa, ya = points[i]
            
            for i2 in range(len(points)):
                if i == i2:
                    continue
                
                xb, yb = points[i2]
                x = abs(xa - xb)
                y = abs(ya - yb)
                adjs[i].add((x + y, i2))
                
        visited = set()
        min_heap = [(0, 0)]  # heap((distance, point), )
        min_distance = 0

        while len(visited) < len(points):
            while min_heap[0][1] in visited:
                heapq.heappop(min_heap)
            distance, point = heapq.heappop(min_heap)
            visited.add(point)
            min_distance += distance

            for adj in adjs[point]:
                if adj[1] not in visited:
                    heapq.heappush(min_heap, adj)

        return min_distance


print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
print(Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)