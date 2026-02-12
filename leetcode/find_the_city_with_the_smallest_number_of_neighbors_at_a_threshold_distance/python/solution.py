import heapq


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        """
        Time complexity: O(n3logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph
        Dijkstra's alg
        """
        adjs = {index: set() for index in range(n)}
        for u, v, distance in edges:
            if distance <= distanceThreshold:
                adjs[u].add((distance, v))
                adjs[v].add((distance, u))

        def dijkstra(distance, city):
            visited = [False] * n
            city_heap = [(distance, city)]

            while city_heap:
                distance, city = heapq.heappop(city_heap)
                if visited[city]:
                    continue
                visited[city] = True

                for adj_distance, adj_city in adjs[city]:
                    if (
                        distance + adj_distance <= distanceThreshold and
                        not visited[adj_city]
                    ):
                        heapq.heappush(city_heap, (distance + adj_distance, adj_city))

            return sum(visited) - 1

        min_neighbors_counter = n
        for city in range(n):
            neighbors_counter = dijkstra(0, city)
            if neighbors_counter <= min_neighbors_counter:
                min_neighbors_counter = neighbors_counter
                min_neighbors_city = city

        return min_neighbors_city


print(Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3)
print(Solution().findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0)
print(Solution().findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20) == 5)
