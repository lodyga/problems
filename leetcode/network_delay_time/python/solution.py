import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V + E)
        Tags: bfs, iteration, graph
        Dijkstra
        """
        next_vertices = {vertex: set() for vertex in range(1, n + 1)}  # {vertex: {(next vertex, weight), ()}, }
        delays = [0] * n  # [[vertex - 1]: min weight, ]
        for source, destnation, time in times:
            next_vertices[source].add((destnation, time))


        visited = set()
        min_heap = [(0, k)]
        
        while len(visited) != n and min_heap:
            weight, vertex = heapq.heappop(min_heap)
            if vertex in visited:
                continue
            delays[vertex - 1] = weight
            visited.add(vertex)

            for next_vertex, next_delay in next_vertices[vertex]:
                heapq.heappush(min_heap, (weight + next_delay, next_vertex))

        # return max(delays) if len(visited) == n else -1
        return weight if len(visited) == n else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(V * E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph
        DFS
        """
        next_vertices = {vertex: set() for vertex in range(1, n + 1)}  # {vertex: {(next vertex, weight), ()}, }
        delays = {vertex: 10**4 + 1 for vertex in range(1, n + 1)}  # {vertex: min weight, }
        for source, destnation, time in times:
            next_vertices[source].add((destnation, time))
        
        def dfs(vertex, weight):
            if delays[vertex] <= weight:
                return
            
            delays[vertex] = weight

            for next_vertex, next_weight in next_vertices[vertex]:
                dfs(next_vertex, weight + next_weight)

        dfs(k, 0)

        max_delay = 0
        for delay in delays.values():
            if delay == 10**4 + 1:
                return -1
            elif delay > max_delay:
                max_delay = delay        
        return max_delay


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2)
print(Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1)
print(Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1)
print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1) == 3)
print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 1]], 3, 2) == -1)