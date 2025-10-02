class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph
        """
        node_count = len(graph)
        is_node_safe = [-1] * node_count

        def dfs(node):
            if is_node_safe[node] != -1:
                return is_node_safe[node]

            is_node_safe[node] = 0

            for adj_node in graph[node]:
                if not dfs(adj_node):
                    is_node_safe[node] = 0
                    return 0

            is_node_safe[node] = 1
            return 1

        return [node for node in range(node_count) if dfs(node)]


print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]), [2, 4, 5, 6])
print(Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]), [4])
print(Solution().eventualSafeNodes([[1, 3, 4, 5], [], [], [], [], [2, 4]]), [0, 1, 2, 3, 4, 5])