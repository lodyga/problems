import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, graph, msp
        Minimum Spanning Tree, Prim's alg
        """
        vertex_size = len(points)
        # frontier map
        adjs = {vertex: set() for vertex in range(vertex_size)}  # {vertex: {(adjacent vertex, distance), ...}, ...}
        for index in range(vertex_size):
            xa, ya = points[index]
            for index2 in range(vertex_size):
                if index2 < index:
                    xb, yb = points[index2]
                    distance = abs(xa - xb) + abs(ya - yb)
                    adjs[index].add((index2, distance))
                    adjs[index2].add((index, distance))

        closest_vertex = [(0, 0)]  # heap((distance, point))
        total_distance = 0
        visited = set()

        while len(visited) < vertex_size:
            distance, vertex = heapq.heappop(closest_vertex)
            if vertex in visited:
                continue
            visited.add(vertex)
            total_distance += distance

            for adj_vertex, adj_distance in adjs[vertex]:
                if adj_vertex not in visited:
                    heapq.heappush(closest_vertex, (adj_distance, adj_vertex))
        
        return total_distance


print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20)
print(Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18)