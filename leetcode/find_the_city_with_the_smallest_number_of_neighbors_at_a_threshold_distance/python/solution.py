class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        import heapq
        """
        Time complexity: O(n3logn)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, hash map, hash set
            A: greedy, Dijkstra
            Model: graph
        """
        adjs = {index: [] for index in range(n)}
        for u, v, distance in edges:
            if distance <= distanceThreshold:
                adjs[u].append((distance, v))
                adjs[v].append((distance, u))

        def dijkstra(distance, city):
            visited = [False] * n
            city_heap = [(distance, city)]

            while city_heap:
                distance, city = heapq.heappop(city_heap)

                if visited[city]:
                    continue

                visited[city] = True

                for adj_distance, adj_city in adjs[city]:
                    if distance + adj_distance <= distanceThreshold:
                        heapq.heappush(city_heap, (distance + adj_distance, adj_city))

            return sum(visited) - 1

        res_city = -1
        min_counter = n
        
        for city in range(n):
            neighbors_counter = dijkstra(0, city)
            if neighbors_counter <= min_counter:
                min_counter = neighbors_counter
                res_city = city

        return res_city


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distance_threshold: int) -> int:
        import heapq
        """
        Time complexity: O(n3logn)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, hash map, hash set
            A: greedy, Dijkstra
            Model: graph
        """
        adjs = [[] for _ in range(n)]
        # heap([(distance, source, destination)])
        dist_heap = []
        visited = {node: {} for node in range(n)}

        for u, v, dist in edges:
            adjs[u].append((v, dist))
            adjs[v].append((u, dist))

        for node in range(n):
            heapq.heappush(dist_heap, (0, node, node))

        # dijkstra
        while dist_heap:
            dist, src, dst = heapq.heappop(dist_heap)

            if dst in visited[src]:
                continue

            visited[src][dst] = dist

            for next_dst, next_dist in adjs[dst]:
                if dist + next_dist <= distance_threshold:
                    heapq.heappush(dist_heap, (dist + next_dist, src, next_dst))

        res_node = n
        res_visits = n + 1
        for node in range(n - 1, -1, -1):
            if len(visited[node]) < res_visits:
                res_node = node
                res_visits = len(visited[node])

        return res_node


print(Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3)
print(Solution().findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0)
print(Solution().findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20) == 5)
