from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: queue, array, hash set
            A: multi-source BFS
            Model: graph
        """
        # one node, no edges
        if n == 1:
            return [0]

        adjs = [[] for _ in range(n)]
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        leaves = deque()
        degree = [len(adj) for adj in adjs]
        for node, adj_nodes in enumerate(adjs):
            if len(adj_nodes) == 1:
                leaves.append(node)

        while n > 2:
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for adj_node in adjs[node]:
                    degree[adj_node] -= 1

                    if degree[adj_node] == 1:
                        leaves.append(adj_node)

        return list(leaves)


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1])
print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4])
print(Solution().findMinHeightTrees(10, [[0, 1], [0, 2], [0, 3], [2, 4], [0, 5], [5, 6], [6, 7], [2, 8], [7, 9]]) == [5])
print(Solution().findMinHeightTrees(1, []) == [0])
