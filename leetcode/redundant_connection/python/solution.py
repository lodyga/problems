class DSU:
    def __init__(self, N) -> None:
        self.size = [1] * N
        self.parent = list(range(N))

    def find(self, vertex):
        # if vertex != self.parent[vertex]:
        #     self.parent[vertex] = self.find(self.parent[vertex])
        # return self.parent[vertex]
        while vertex != self.parent[vertex]:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return True
        elif self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DSU, cycle detection
        """
        dsu = DSU(len(edges))

        for u, v in edges:
            if dsu.union(u - 1, v - 1):
                return [u, v]


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3])
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4])
print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]) == [2, 5])
