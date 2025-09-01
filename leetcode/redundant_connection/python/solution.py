class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        parents = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(vertex):
            while vertex != parents[vertex]:
                parents[vertex] = parents[parents[vertex]]
                vertex = parents[vertex]
            return vertex

        def union(vertex1, vertex2):
            parent1 = find(vertex1)
            parent2 = find(vertex2)

            if parent1 == parent2:
                return True
            elif rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                rank[parent1] += rank[parent2]
                parents[parent2] = vertex1

        for vertex1, vertex2 in edges:
            if union(vertex1, vertex2):
                return [vertex1, vertex2]


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]), [2, 5])