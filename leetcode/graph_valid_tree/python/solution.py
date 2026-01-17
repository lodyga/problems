from collections import deque


class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: Single-source DFS, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        adj_vertices = {vertex: set() for vertex in range(vertex_count)}
        for u, v in edges:
            adj_vertices[u].add(v)
            adj_vertices[v].add(u)

        visited = [False] * vertex_count

        def dfs(vertex: int, prev: int) -> bool:
            if visited[vertex]:
                return False

            visited[vertex] = True

            for adj_vertex in adj_vertices[vertex]:
                if (
                    adj_vertex != prev and
                    dfs(adj_vertex, vertex) is False
                ):
                    return False

            return True

        # No cycles and connected.
        return dfs(0, -1) and all(visited)


class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: Single-source BFS, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        adj_vertices = {vertex: set() for vertex in range(vertex_count)}
        for u, v in edges:
            adj_vertices[u].add(v)
            adj_vertices[v].add(u)

        visited = [False] * vertex_count

        def bfs() -> bool:
            queue = deque([(0, -1)])
            while queue:
                vertex, prev = queue.popleft()

                if visited[vertex]:
                    return False
                visited[vertex] = True

                for adj_vertex in adj_vertices[vertex]:
                    if adj_vertex != prev:
                        queue.append((adj_vertex, vertex))

            return True

        # No cycles and connected.
        return bfs() and all(visited)


class DSU:
    def __init__(self, N) -> None:
        self.size = [1] * N
        self.parent = list(range(N))

    def find(self, vertex: int) -> int:
        while vertex != self.parents[vertex]:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex
    
    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = self.parent[pu]
            self.parent[v] = self.parent[pu]
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = self.parent[pv]
            self.parent[u] = self.parent[pv]
        
        return True


class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DSU, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        dsu = DSU(vertex_count)
        for u, v in edges:
            if dsu.union(u, v) is False:
                return False
        
        return True


print(Solution().validTree(3, [[0, 1], [1, 2], [2, 0]]) == False)
print(Solution().validTree(1, [[0, 0]]) == False)
print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False)
print(Solution().validTree(4, [[0, 1], [2, 3]]) == False)
print(Solution().validTree(5, [[0, 1], [2, 0], [3, 0], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 3], [3, 2], [1, 4]]) == True)
print(Solution().validTree(1, []) == True)
print(Solution().validTree(5, [[0, 1], [1, 3], [3, 0], [2, 4]]) == False)
