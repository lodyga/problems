import heapq


class Solution:
    def findCheapestPrice(self, N: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(Elog(V*k))
        Auxiliary space complexity: O(V*k)
        Tags:
            DS: heap, hash map, hash set, array
            A: greedy, Dijkstra with cache
            Model: graph
        """
        UPPER_BOUND = 10**6
        cache = [[UPPER_BOUND] * (k + 2) for _ in range(N)]
        adj_vertices = [[] for _ in range(N)]

        for source, destination, price in flights:
            adj_vertices[source].append((destination, price))

        # heap((price, vertex, transits))
        flight_heap = [(0, src, 0)]

        while flight_heap:
            price, vertex, transits = heapq.heappop(flight_heap)

            if vertex == dst:
                return price
            elif (
                transits == k + 1 or
                price > cache[vertex][transits]
            ):
                continue

            for adj_vertex, adj_price in adj_vertices[vertex]:
                partial_price = price + adj_price

                if partial_price < cache[adj_vertex][transits + 1]:
                    cache[adj_vertex][transits + 1] = partial_price
                    heapq.heappush(
                        flight_heap,
                        (partial_price, adj_vertex, transits + 1)
                    )

        return -1



class Solution:
    def findCheapestPrice(self, N: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(E*k)
            O(E*V) => O(E*V)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: BFS, Bellman-Ford
            Model: graph
        """
        COST_BOUND = 10**6
        price_cache = [COST_BOUND] * N
        price_cache[src] = 0

        for _ in range(k + 1):
            cache_copy = price_cache.copy()

            for source, destination, price in flights:
                if price_cache[source] == COST_BOUND:
                    continue
                
                elif price_cache[source] + price < cache_copy[destination]:
                    cache_copy[destination] = price_cache[source] + price

            price_cache = cache_copy

        return (
            price_cache[dst]
            if price_cache[dst] != COST_BOUND
            else -1
        )


print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500)
print(Solution().findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1) == -1)
print(Solution().findCheapestPrice(5, [[1, 0, 5], [2, 1, 5], [3, 0, 2], [1, 3, 2], [4, 1, 1], [2, 4, 1]], 2, 0, 2) == 7)
print(Solution().findCheapestPrice(11, [[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2], [6, 1, 100], [0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1], [10, 2, 1], [1, 2, 100]], 0, 2, 4) == 11)
print(Solution().findCheapestPrice(13, [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]], 10, 1, 10) == -1)
