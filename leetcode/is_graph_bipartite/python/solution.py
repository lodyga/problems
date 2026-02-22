class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        from collections import deque
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V)
        Tags:
            DS: array, queue
            A: BFS
            Model: graph
        """
        N = len(graph)
        # 0: not visited, 1/-1: two colors
        colored = [0] * N

        def bfs(node):
            if colored[node]:
                return True
            
            color = 1
            queue = deque([(node, color)])
            colored[node] = color

            while queue:
                node, color = queue.popleft()

                for adj_node in graph[node]:
                    if colored[adj_node] == color:
                        return False
                    elif colored[adj_node]:
                        continue

                    queue.append((adj_node, -color))
                    colored[adj_node] = -color
            
            return True

        for node in range(N):
            if colored[node] == 0:
                if bfs(node) == False:
                    return False

        return True


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V)
        Tags:
            DS: array
            A: DFS
            Model: graph
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

            for adj_node in graph[node]:
                if dfs(adj_node, not which_set) is False:
                    return False

            return True

        for node in range(N):
            if dfs(node, node in set_a) is False:
                return False

        return True


print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False)
print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True)
print(Solution().isBipartite([[1], [0, 3], [3], [1, 2]]) == True)
print(Solution().isBipartite([[4], [], [4], [4], [0, 2, 3]]) == True)
print(Solution().isBipartite([[1], [0], [4], [4], [2, 3]]) == True)
print(Solution().isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]) == False)
