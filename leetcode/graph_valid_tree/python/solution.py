class Solution:
    def validTree(self, node_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: backtracking, dfs, recursion
        DFS
        """
        if len(edges) > node_count - 1:
            return False
        
        adjs = {vertex: set() for vertex in range(n)}
        for u, v in edges:
            if u == v:
                return False
            adjs[u].add(v)
            adjs[v].add(u)

        visited = set()

        def dfs(vertex, prev_vertex):
            if vertex in visited:
                return False

            visited.add(vertex)

            for adj_vertex in adjs[vertex]:
                if (
                    adj_vertex != prev_vertex and 
                    not dfs(adj_vertex, vertex)
                ):
                    return False

            return True
        
        # no cycles and connected
        return dfs(0, -1) and len(visited) == node_count


from collections import deque


class Solution:
    def validTree(self, node_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: backtracking, bfs, iteration
        BFS
        """
        if len(edges) > node_count - 1:
            return False
        
        adjs = {vertex: set() for vertex in range(node_count)}
        for u, v in edges:
            if u == v:
                return False
            adjs[u].add(v)
            adjs[v].add(u)

        queue = deque([(0, -1)])
        visited = set()

        def bfs():
            while queue:
                node, parent_node = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)

                for next_node in adjs[node]:
                    if next_node != parent_node:
                        queue.append((next_node, node))
            
            return len(visited) == node_count

        return bfs()


class DSU:
    def __init__(self, node_count) -> None:
        self.parents = list(range(node_count))
        self.rank = [1] * node_count
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
            return False
        elif self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
            self.parents[v] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
            self.parents[u] = pv
        self.size -= 1
        return True

class Solution:
    def validTree(self, node_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        if len(edges) > node_count - 1:
            return False
        
        dsu = DSU(node_count)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return dsu.size == 1


print(Solution().validTree(3, [[0, 1], [1, 2], [2, 0]]) == False)
print(Solution().validTree(1, [[0, 0]]) == False)
print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False)
print(Solution().validTree(4, [[0, 1], [2, 3]]) == False)
print(Solution().validTree(5, [[0, 1], [2, 0], [3, 0], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 3], [3, 2], [1, 4]]) == True)
print(Solution().validTree(1, []) == True)