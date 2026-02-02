class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DFS with memoization, cycle detection
            Model: graph
        """
        N = len(graph)
        # -1: not visited, 1: safe/terminal node, 0: unsafe/visiting stack node
        is_node_safe = [-1] * N

        def dfs(node: int) -> int:
            if is_node_safe[node] != -1:
                return is_node_safe[node]

            is_node_safe[node] = 0
            
            for next_node in graph[node]:
                if dfs(next_node) == 0:
                    return 0
                
            is_node_safe[node] = 1
            return 1
        
        return [node for node in range(N) if dfs(node)]


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        from typing import Optional
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DFS with memoization, cycle detection
            Model: graph
        """
        N = len(graph)
        # None: not visited, True: safe/terminal node, False: unsafe/visiting stack node
        is_node_safe: list[Optional[bool]] = [None] * N

        def dfs(node: int) -> bool:
            if is_node_safe[node] is not None:
                return bool(is_node_safe[node])

            is_node_safe[node] = False

            for next_node in graph[node]:
                if not dfs(next_node):
                    return False

            is_node_safe[node] = True
            return True

        return [node for node in range(N) if dfs(node)]


print(sorted(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])) == sorted([2, 4, 5, 6]))
print(sorted(Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []])) == sorted([4]))
print(sorted(Solution().eventualSafeNodes([[1, 3, 4, 5], [], [], [], [], [2, 4]])) == sorted([0, 1, 2, 3, 4, 5]))
