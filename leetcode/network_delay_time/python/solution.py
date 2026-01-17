import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: heap, hash map, hash set, graph
            A: BFS, Dijkstra
        """
        # {vertex: set((next vertex, time to travel), ), }
        next_vertices = {vertex: set() for vertex in range(n)}

        for scr, dst, time in times:
            next_vertices[scr - 1].add((dst - 1, time))

        vertex_heap = [(0, k - 1)]
        visited = [False] * n
        max_delay = -1
        
        while vertex_heap:
            time, vertex = heapq.heappop(vertex_heap)
            if visited[vertex]:
                continue
            visited[vertex] = True
            max_delay = max(max_delay, time)

            for next_vertex, next_time in next_vertices[vertex]:
                if not visited[next_vertex]:
                    heapq.heappush(vertex_heap, (time + next_time, next_vertex))

        return max_delay if all(visited) else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(V * E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: hash map, hash set, graph
            A: DFS
        """
        # {vertex: set((next vertex, delay), ), }
        next_vertices = {vertex: set() for vertex in range(n)}
        # {vertex: min delay, }
        delays = {vertex: 10**4 + 1 for vertex in range(n)}
        for src, dst, time in times:
            next_vertices[src - 1].add((dst - 1, time))
        
        def dfs(vertex, weight):
            if delays[vertex] <= weight:
                return
            
            delays[vertex] = weight

            for next_vertex, next_weight in next_vertices[vertex]:
                dfs(next_vertex, weight + next_weight)

        dfs(k - 1, 0)

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
