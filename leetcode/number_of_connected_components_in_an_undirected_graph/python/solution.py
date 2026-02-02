from collections import deque


class Solution:
    def countComponents(self, N: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source DFS
            Model: graph
        """
        components = 0
        visited = [False] * N
        adjs = {node: set() for node in range(N)}

        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)

        def dfs(node: int) -> int:
            if visited[node]:
                return 0

            visited[node] = True

            for adj_node in adjs[node]:
                dfs(adj_node)

            return 1

        for node in range(N):
            components += dfs(node)

        return components


class Solution:
    def countComponents(self, N: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source BFS
            Model: graph
        """
        components = 0
        visited = [False] * N
        adjs = {node: set() for node in range(N)}

        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)

        def bfs(node: int) -> int:
            if visited[node]:
                return 0
            queue = deque([node])

            while queue:
                node = queue.popleft()
                visited[node] = True

                for adj_node in adjs[node]:
                    if not visited[adj_node]:
                        queue.append(adj_node)

            return 1

        for node in range(N):
            components += bfs(node)

        return components


class DSU:
    def __init__(self, N) -> None:
        self.size = [1] * N
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
            return
        elif self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = self.parent[pu]
            self.components -= 1
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = self.parent[pv]
            self.components -= 1


class Solution:
    def countComponents(self, N: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DSU
            Model: graph
        """
        dsu = DSU(N)

        for u, v in edges:
            dsu.union(u, v)

        return dsu.components


print(Solution().countComponents(3, [[0, 1], [0, 2]]) == 1)
print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2)
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1)
print(Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) == 2)
