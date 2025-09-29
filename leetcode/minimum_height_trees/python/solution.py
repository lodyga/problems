from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: bfs, iteration, graph
        """
        # one node, no edges
        if n == 1:
            return [0]

        adjs = {node: set() for node in range(n)}
        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)

        edge_counter = {}
        leaves = deque()
        for node, neighbous in adjs.items():
            edge_counter[node] = len(neighbous)
            if len(neighbous) == 1:
                leaves.append(node)

        while n > 2:
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbour in adjs[node]:
                    edge_counter[neighbour] -= 1
                    if edge_counter[neighbour] == 1:
                        leaves.append(neighbour)

        return list(leaves)
    

print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1])
print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4])
print(Solution().findMinHeightTrees(10, [[0, 1], [0, 2], [0, 3], [2, 4], [0, 5], [5, 6], [6, 7], [2, 8], [7, 9]]) == [5])