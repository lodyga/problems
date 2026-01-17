from collections import deque


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix side
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (graph)
            A: multi-source DFS
        """
        N = len(is_connected)
        components = 0
        visited = [False] * N

        def dfs(node: int) -> int:
            if visited[node]:
                return 0

            visited[node] = True

            for index in range(N):
                if (
                    index != node and
                    is_connected[node][index]
                ):
                    dfs(index)

            return 1

        for node in range(N):
            components += dfs(node)

        return components


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array (graph)
            A: multi-source BFS
        """
        N = len(is_connected)
        components = 0
        visited = [False] * N

        def bfs(node: int) -> int:
            if visited[node]:
                return 0
            queue = deque([node])

            while queue:
                node = queue.popleft()
                visited[node] = True

                for index in range(N):
                    if (
                        index != node and
                        is_connected[node][index] and
                        not visited[index]
                    ):
                        queue.append(index)

            return 1

        for node in range(N):
            components += bfs(node)

        return components


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix side
        Auxiliary space complexity: O(n)
        Tags:
            DS: array (graph)
            A: DSU
        """
        N = len(is_connected)
        dsu = DSU(N)

        for u in range(N):
            for v in range(N):
                if u > v and is_connected[u][v]:
                    dsu.union(u, v)

        return dsu.components


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


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)
print(Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1)
