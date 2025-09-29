class DSU:
    def __init__(self, node_count) -> None:
        self.rank = [1] * node_count
        self.parents = list(range(node_count))

    def find(self, node):
        # while node != self.parents[node]:
        #     self.parents[node] = self.parents[self.parents[node]]
        #     node = self.parents[node]
        # return node
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return True
        elif pu >= pv:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
        return False


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        dsu = DSU(len(edges))
        for u, v in edges:
            if dsu.union(u - 1, v - 1):
                return [u , v]


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3])
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4])
print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]) == [2, 5])