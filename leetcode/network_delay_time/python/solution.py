import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(V * E)
        Auxiliary space complexity: O(V + E)
        Tags: Dijkstra
        """
        next_vertexes = {index: set() for index in range(1, n + 1)}
        for u, v, w in times:
            next_vertexes[u].add((v, w))

        min_heap = [(0, k)]
        visited = set()
        min_time = 0

        while min_heap:
            weight, vertex = heapq.heappop(min_heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            min_time = weight

            for next_vertex, next_weight in next_vertexes[vertex]:
                if next_vertex in visited:
                    continue
                heapq.heappush(min_heap, (weight + next_weight, next_vertex))

        return min_time if len(visited) == n else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Time complexity: O(ElogV)
        Auxiliary space complexity: O(V + E)
        Tags: dfs
        """
        N = 10**4 + 1  # unreachable value for n

        next_vertexes = {index: set() for index in range(1, n + 1)}
        for u, v, w in times:
            next_vertexes[u].add((v, w))

        visited = {index: N for index in range(1, n + 1)}

        def dfs(vertex, weight):
            if visited[vertex] <= weight:
                return

            visited[vertex] = weight

            for next_vertex, next_weight in next_vertexes[vertex]:
                dfs(next_vertex, weight + next_weight)

        dfs(k, 0)
        
        min_time = 0
        for value in visited.values():
            if value == N:
                return -1
            min_time = max(min_time, value)
        return min_time


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2)
print(Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1)
print(Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1)
print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1) == 3)
print(Solution().networkDelayTime([[1, 2, 1], [2, 3, 1]], 3, 2) == -1)