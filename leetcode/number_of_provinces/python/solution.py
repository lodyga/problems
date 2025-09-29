class DSU:
    def __init__(self, node_count) -> None:
        self.rank = [1] * node_count
        self.parents = list(range(node_count))
        self.size = node_count

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        elif self.rank[pv] > self.rank[pu]:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
        else:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
        self.size -= 1


class Solution:
    def findCircleNum(self, connections: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix len
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        node_count = len(connections)
        dsu = DSU(node_count)

        for row in range(node_count):
            for col in range(node_count):
                if (row > col and connections[row][col]):
                    dsu.union(row, col)

        return dsu.size


class Solution:
    def findCircleNum(self, connections: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix len
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DFS
        """
        node_count = len(connections)
        adjs = {node: set() for node in range(node_count)}
        for row in range(node_count):
            for col in range(node_count):
                if row > col and connections[row][col]:
                    adjs[row].add(col)
                    adjs[col].add(row)

        visited = [False] * node_count
        province_count = 0

        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True
            
            for adj_node in adjs[node]:
                dfs(adj_node)
            
        
        for province in range(node_count):
            if not visited[province]:
                dfs(province)
                province_count += 1

        return province_count


from collections import deque


class Solution:
    def findCircleNum(self, connections: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
            n: adjacency matrix len
        Auxiliary space complexity: O(n)
        Tags: bfs, dfs, graph, dsu
        BFS
        """
        node_count = len(connections)
        adjs = {node: set() for node in range(node_count)}
        for row in range(node_count):
            for col in range(node_count):
                if row > col and connections[row][col]:
                    adjs[row].add(col)
                    adjs[col].add(row)

        visited = [False] * node_count
        province_count = 0

        def bfs(province):
            queue = deque([province])
            while queue:
                node = queue.popleft()
                visited[node] = True

                for adj_node in adjs[node]:
                    if not visited[adj_node]:
                        queue.append(adj_node)

        for province in range(node_count):
            if not visited[province]:
                bfs(province)
                province_count += 1
        
        return province_count


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)