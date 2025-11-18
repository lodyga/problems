from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V)
        Tags: dfs, recursion, graph
        """
        N = len(graph)
        set_a = set()
        set_b = set()

        def dfs(node, which_set):
            if which_set:
                current_set = set_a
                opposite_set = set_b
            else:
                current_set = set_b
                opposite_set = set_a

            if node in opposite_set:
                return False
            elif node in current_set:
                return True

            current_set.add(node)

            for next_node in graph[node]:
                if dfs(next_node, not which_set) is False:
                    return False

            return True

        for node in range(N):
            if dfs(node, node in set_a) is False:
                return False

        return True


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V)
        Tags: bfs, iteration, graph
        """
        N = len(graph)
        set_a = set()
        set_b = set()

        def bfs(node, which_set):
            if node in set_a or node in set_b:
                return True

            queue = deque([(node, which_set)])
            set_b.add(node)

            while queue:
                node, which_set = queue.popleft()
                if which_set:
                    current_set = set_a
                    opposite_set = set_b
                else:
                    current_set = set_b
                    opposite_set = set_a

                for next_node in graph[node]:
                    if next_node in current_set:
                        return False
                    elif next_node not in opposite_set:
                        queue.append((next_node, not which_set))
                        opposite_set.add(next_node)

        for node in range(N):
            if bfs(node, node in set_a) is False:
                return False

        return True


print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False)
print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True)
print(Solution().isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]) == False)
print(Solution().isBipartite([[1], [0, 3], [3], [1, 2]]) == True)
