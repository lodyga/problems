from collections import deque


class DSU:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))
        self.components = n

    def find(self, u) -> int:
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v) -> None:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        elif self.size[pv] > self.size[pu]:
            (pu, pv) = (pv, pu)

        self.size[pu] += self.size[pv]
        self.parent[pv] = self.parent[pu]
        self.components -= 1


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DSU
            Model: graph
        """
        dsu = DSU(n)

        for (u, v) in edges:
            dsu.union(u, v)

        return dsu.components


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source DFS
            Model: graph
        """
        def dfs(node: int) -> int:
            if visited[node]:
                return 0

            visited[node] = True

            for adj_node in adj_nodes[node]:
                dfs(adj_node)

            return 1

        components = 0
        visited = [False] * n
        adj_nodes = [[] for node in range(n)]

        for u, v in edges:
            adj_nodes[u].append(v)
            adj_nodes[v].append(u)

        for node in range(n):
            components += dfs(node)

        return components


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: queue, array
            A: multi-source BFS
            Model: graph
        """
        def bfs(node: int) -> int:
            if visited[node]:
                return 0

            queue = deque([node])
            visited[node] = True

            while queue:
                node = queue.popleft()

                for adj_node in adj_nodes[node]:
                    if not visited[adj_node]:
                        queue.append(adj_node)
                        visited[adj_node] = True

            return 1

        visited = [False] * n
        adj_nodes = [[] for node in range(n)]
        components = 0

        for u, v in edges:
            adj_nodes[u].append(v)
            adj_nodes[v].append(u)

        for node in range(n):
            components += bfs(node)

        return components


print(Solution().countComponents(3, [[0, 1], [0, 2]]) == 1)
print(Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) == 2)
print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2)
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1)
