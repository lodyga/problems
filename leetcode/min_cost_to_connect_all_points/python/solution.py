import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(V2logV)
        Auxiliary space complexity: O(V2)
        Tags:
            DS: heap, hash map, hash set
            A: greedy, MST, Prim
            Model: graph
        """
        N = len(points)
        # frontier map
        # {vertex: set((adjecent vertex, distance), ), }
        adj_vertices = [[] for _ in range(N)]

        for u, (x1, y1) in enumerate(points):
            for v, (x2, y2) in enumerate(points):
                if u > v:
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    adj_vertices[u].append((v, distance))
                    adj_vertices[v].append((u, distance))

        visited = [False] * N
        edge_counter = 0
        total_distance = 0
        # heap((distance, vertex), )
        vertex_heap = [(0, 0)]

        while edge_counter < N:
            distance, vertex = heapq.heappop(vertex_heap)

            if visited[vertex]:
                continue
            visited[vertex] = True
            edge_counter += 1
            total_distance += distance

            for adj_vertex, adj_distance in adj_vertices[vertex]:
                if not visited[adj_vertex]:
                    heapq.heappush(vertex_heap, (adj_distance, adj_vertex))

        return total_distance



class DSU:
    def __init__(self, N):
        self.size = [1] * (N)
        self.parent = list(range(N))
        self.components = N

    def find(self, vertex):
        while self.parent[vertex] != vertex:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        elif self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = self.parent[pu]
        else:
                self.size[pv] += self.size[pu]
            self.parent[pu] = self.parent[pv]

        self.components -= 1
        return True


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(V2logV)
        Auxiliary space complexity: O(V2)
        Tags:
            DS: heap, array
            A: DSU, MST, Kruskal
            Model: graph
        """
        N = len(points)
        dsu = DSU(N)
        edges = []

        for u, (x1, y1) in enumerate(points):
            for v, (x2, y2) in enumerate(points):
                if u > v:
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    # edges.append((distance, u, v))
                    heapq.heappush(edges, (distance, u, v))

        # O(ElogE) => O(V2logV2) => O(V2logV)
        # edges.sort()
        total_distance = 0

        index = 0
        while dsu.components > 1:
            # distance, u, v = edges[index]
            distance, u, v = heapq.heappop(edges)
            if dsu.union(u, v):
                total_distance += distance
            index += 1

        return total_distance


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(V2)
        Auxiliary space complexity: O(V)
        Tags:
            DS: hash map, hash set
            A: greedy, MST, Prim
            Model: graph
        """
        def dist(u, v):
            x1, y1 = points[u]
            x2, y2 = points[v]
            return abs(x1 - x2) + abs(y1 - y2)

        N = len(points)
        visited = [False] * N
        min_dist = [10**9] * N

        min_dist[0] = 0
        total_dist = 0

        for _ in range(N):
            # 1. pick closest unvisited vertex
            u = -1
            for i in range(N):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            total_dist += min_dist[u]

            # 2. relax edges
            for v in range(N):
                if not visited[v]:
                    min_dist[v] = min(min_dist[v], dist(u, v))

        return total_dist


print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20)
print(Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18)
print(Solution().minCostConnectPoints([[0, 0]]) == 0)
print(Solution().minCostConnectPoints([[11, 12], [-9, 5], [-1, 5], [9, -8], [20, -17], [18, 19], [-1, 14], [16, 19], [2, 16], [14, 3], [1, -12], [19, 4], [5, -17], [-13, 6], [-4, 1], [-7, -16], [13, 7], [-20, -7], [20, -15]]) == 165)
