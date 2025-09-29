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
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        dsu = DSU(node_count)
        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.size


class Solution:
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        DFS
        """
        adjs = {node: set() for node in range(node_count)}
        for u, v in edges:
            if u != v:
                adjs[u].add(v)
                adjs[v].add(u)
        
        visited = [False] * node_count
        component_count = 0

        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True

            for adj_node in adjs[node]:
                dfs(adj_node)

        for node in range(node_count):
            if not visited[node]:
                dfs(node)
                component_count += 1
        
        return component_count


from collections import deque


class Solution:
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        BFS
        """
        adjs = {node: set() for node in range(node_count)}
        for u, v in edges:
            if u != v:
                adjs[u].add(v)
                adjs[v].add(u)
        
        visited = [False] * node_count
        component_count = 0

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited[node] = True

                for adj_node in adjs[node]:
                    if not visited[adj_node]:
                        queue.append(adj_node)

        for node in range(node_count):
            if not visited[node]:
                bfs(node)
                component_count += 1
        
        return component_count


print(Solution().countComponents(3, [[0, 1], [0, 2]]), 1)
print(Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]), 2)