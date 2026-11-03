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
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix side
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: DSU
            Model: graph
        """
        n = len(is_connected)
        dsu = DSU(n)

        for u in range(n):
            for v in range(n):
                if u > v and is_connected[u][v]:
                    dsu.union(u, v)

        return dsu.components


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix side
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: multi-source DFS
            Model: graph
        """
        def dfs(node: int) -> int:
            if visited[node]:
                return 0

            visited[node] = True

            for adj_node in range(n):
                if (adj_node != node and is_connected[node][adj_node]):
                    dfs(adj_node)

            return 1

        n = len(is_connected)
        components = 0
        visited = [False] * n

        for node in range(n):
            components += dfs(node)

        return components


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: queue, array
            A: multi-source BFS
            Model: graph
        """
        n = len(is_connected)
        visited = [False] * n
        components = 0

        def bfs(node: int) -> int:
            if visited[node]:
                return 0

            queue = deque([node])
            visited[node] = True

            while queue:
                node = queue.popleft()

                for adj_node in range(n):
                    if (
                        adj_node != node
                        and is_connected[node][adj_node]
                        and not visited[adj_node]
                    ):
                        queue.append(adj_node)
                        visited[adj_node] = True

            return 1

        for node in range(n):
            components += bfs(node)

        return components


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)
print(Solution().findCircleNum(
    [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1)
