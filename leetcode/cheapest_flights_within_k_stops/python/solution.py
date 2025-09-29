import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V+E)
        Tags: bfs, iteration, graph
        Dijkstra with memo
        """
        adjs = [set() for _ in range(n)]
        for source, destination, cost in flights:
            adjs[source].add((cost, destination))

        min_heap = []  # (cost, transfers, vertex)
        heapq.heappush(min_heap, (0, -1, src))
        # vertex min travel cost, {(node, transfers): min const, }
        # vertex_cost_map = {}
        vertex_cost_map = [[10**6] * (k + 1) for _ in range(n)]

        while min_heap:
            cost, transfers, vertex = heapq.heappop(min_heap)
            if vertex == dst:
                return cost
            elif transfers == k:
                continue

            for adj_cost, adj_vertex in adjs[vertex]:
                to_adj_cost = cost + adj_cost
                # if vertex_cost_map.get((adj_vertex, transfers + 1), 10**6) > to_adj_cost:
                #     vertex_cost_map[(adj_vertex, transfers + 1)] = to_adj_cost
                if vertex_cost_map[adj_vertex][transfers + 1] > to_adj_cost:
                    vertex_cost_map[adj_vertex][transfers + 1] = to_adj_cost
                    heapq.heappush(min_heap, (to_adj_cost, transfers + 1, adj_vertex))

        return -1


class Solution2:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V+E)
        Tags: bfs, iteration, graph, tle
        Dijkstra
        """
        adjs = {flight: set()
                for flight in range(n)}  # {flight: (destination, cost)}
        for s, d, c in flights:
            adjs[s].add((d, c))

        min_heap = [(0, 0, src)]  # heap((cost, stops, vertex))
        # need to visit the same node multiple times
        # visited = set()

        while min_heap:
            cost, stops, vertex = heapq.heappop(min_heap)
            if vertex == dst:
                return cost
            elif stops == k + 1:
                continue

            for adj_dst, adj_cost in adjs[vertex]:
                heapq.heappush(min_heap, (cost + adj_cost, stops + 1, adj_dst))

        return -1


class Solution2:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(E*k)
        Auxiliary space complexity: O(V + E)
        Tags: Bellman-Ford
        """
        TRAVEL_COST_BOUND = 10**6
        adjs = {flight: set()
                for flight in range(n)}  # {flight: (destination, cost)}
        for s, d, c in flights:
            adjs[s].add((d, c))

        to_city_cost = [TRAVEL_COST_BOUND] * n
        to_city_cost[src] = 0

        for _ in range(k + 1):
            layer_to_city_cost = to_city_cost.copy()

            for city in range(n):
                if to_city_cost[city] == TRAVEL_COST_BOUND:
                    continue

                for adj_city, adj_cost in adjs[city]:
                    if to_city_cost[city] + adj_cost < layer_to_city_cost[adj_city]:
                        layer_to_city_cost[adj_city] = to_city_cost[city] + adj_cost

            to_city_cost = layer_to_city_cost

        return (
            to_city_cost[dst]
            if to_city_cost[dst] != TRAVEL_COST_BOUND
            else -1
        )


print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500)
print(Solution().findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1) == -1)
print(Solution().findCheapestPrice(5, [[1, 0, 5], [2, 1, 5], [3, 0, 2], [1, 3, 2], [4, 1, 1], [2, 4, 1]], 2, 0, 2) == 7)
print(Solution().findCheapestPrice(11, [[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2], [6, 1, 100], [0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1], [10, 2, 1], [1, 2, 100]], 0, 2, 4) == 11)
print(Solution().findCheapestPrice(13, [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]], 10, 1, 10) == -1)