import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V+E)
        Tags: Dijkstra, tle
        """
        adjs = {flight: set()
                for flight in range(n)}  # {flight: (destination, cost)}
        for s, d, c in flights:
            adjs[s].add((d, c))

        min_heap = [(0, 0, src)]  # heap((cost, stops, source))
        visited = set()

        while min_heap:
            while min_heap[0][2] in visited:
                heapq.heappop(min_heap)

            cost, stops, source = heapq.heappop(min_heap)

            if source == dst:
                return cost
            elif stops == k + 1:
                continue

            for next_dst, next_cost in adjs[source]:
                heapq.heappush(
                    min_heap, (cost + next_cost, stops + 1, next_dst))

        return -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(E*k)
        Auxiliary space complexity: O(V+E)
        Tags: Bellman Ford alg
        """
        TRAVEL_COST_BOUND = 5*10**7
        adjs = {flight: set()
                for flight in range(n)}  # {flight: (destination, cost)}
        for s, d, c in flights:
            adjs[s].add((d, c))

        travel_costs = [TRAVEL_COST_BOUND] * n
        travel_costs[src] = 0

        for _ in range(k + 1):
            layer_travel_costs = travel_costs.copy()

            for city in range(n):
                if travel_costs[city] == TRAVEL_COST_BOUND:
                    continue

                for adj_city, adj_cost in adjs[city]:
                    if travel_costs[city] + adj_cost < layer_travel_costs[adj_city]:
                        layer_travel_costs[adj_city] = travel_costs[city] + adj_cost
                        pass

            travel_costs = layer_travel_costs

        return (
            travel_costs[dst]
            if travel_costs[dst] != TRAVEL_COST_BOUND
            else -1
        )


print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500)
print(Solution().findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1) == -1)
print(Solution().findCheapestPrice(13, [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]], 10, 1, 10) == -1)
print(Solution().findCheapestPrice(5, [[1, 0, 5], [2, 1, 5], [3, 0, 2], [1, 3, 2], [4, 1, 1], [2, 4, 1]], 2, 0, 2) == 7)