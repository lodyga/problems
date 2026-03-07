class DSU:
    def __init__(self, N: int) -> None:
        self.size = [1] * N
        self.parent = list(range(N))
        self.components = N

    def find(self, u: int) -> int:
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        elif self.size[pu] < self.size[pv]:
            (pu, pv) = (pv, pu)

        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        self.components -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(E2)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: list
            A: DSU, MST, Kruskal
            Model: graph
        """
        for index, edge in enumerate(edges):
            # [u, v, wegith, index]
            edge.append(index)

        edges.sort(key=lambda edge: edge[2])
        mst_weight = 0
        dsu = DSU(n)

        for u, v, weight, index in edges:
            if dsu.union(u, v):
                mst_weight += weight

        critital_edges = []
        pseudo_edges = []
        for u, v, weight, index in edges:
            mst_weight2 = 0
            dsu = DSU(n)

            # Create MST without (u2, v2) edge.
            for u2, v2, weight2, index2 in edges:
                if index != index2 and dsu.union(u2, v2):
                    mst_weight2 += weight2

            if dsu.components != 1 or mst_weight2 > mst_weight:
                critital_edges.append(index)
                continue

            # Create MST with (u2, v2) edge.
            dsu = DSU(n)
            dsu.union(u, v)
            mst_weight2 = weight

            for u2, v2, weight2, index2 in edges:
                if dsu.union(u2, v2):
                    mst_weight2 += weight2

            if mst_weight2 == mst_weight:
                pseudo_edges.append(index)

        return [critital_edges, pseudo_edges]


print(Solution().findCriticalAndPseudoCriticalEdges(5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]) == [[0, 1], [2, 3, 4, 5]])
print(Solution().findCriticalAndPseudoCriticalEdges(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]) == [[], [0, 1, 2, 3]])
