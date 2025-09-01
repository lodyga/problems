class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DSU
        """

        component_count = n
        parents = list(range(n))
        rank = [1] * n
        
        def find(vertex):
            if vertex != parents[vertex]:
                parents[vertex] = parents[parents[vertex]]
                vertex = parents[vertex]
            return vertex
        
        def union(vertex1, vertex2):
            parent1 = find(vertex1)
            parent2 = find(vertex2)

            if parent1 == parent2:
                return 0
            elif rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
                rank[vertex2] += rank[vertex1]
            else:
                parents[parent2] = parent1
                rank[vertex1] += rank[vertex2]
            return 1

        for vertex1, vertex2 in edges:
            component_count -= union(vertex1, vertex2)

        return component_count


class Solution2:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DFS
        """
        component_count = 0
        visited = [False] * n

        # adjacencies
        adjs = {component: set() for component in range(n)}
        for vertex1, vertex2 in edges:
            adjs[vertex1].add(vertex2)
            adjs[vertex2].add(vertex1)

        def dfs(vertex):
            if visited[vertex]:
                return
            
            visited[vertex] = True
            
            for adj_vertex in adjs[vertex]:
                dfs(adj_vertex)
            
            
        for vertex in adjs:
            if not visited[vertex]:
                component_count += 1
                dfs(vertex)
        
        return component_count


print(Solution().countComponents(3, [[0, 1], [0, 2]]), 1)
print(Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]), 2)