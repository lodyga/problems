class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node | None:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: hash map
            A: dfs, recursion
            Model: graph
        """
        copy_map = {}

        def dfs(node):
            if node in copy_map:
                return copy_map[node]

            node_copy = Node(node.val)
            copy_map[node] = node_copy

            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))

            return node_copy

        return dfs(node) if node else None


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: hash map
            A: bfs, iteration
            Model: graph
        """
        from collections import deque
        if node is None:
            return None
        
        # Old node to new node map.
        copy_map = {}
        
        def bfs(node):
            queue = deque([node])
            copy_map[node] = Node(node.val)

            while queue:
                node = queue.popleft()
                node_copy = copy_map[node]

                for neighbor_node in node.neighbors:
                    if neighbor_node not in copy_map:
                        copy_map[neighbor_node] = Node(neighbor_node.val)
                        queue.append(neighbor_node)
                    
                    node_copy.neighbors.append(copy_map[neighbor_node])
        
        bfs(node)
        return copy_map[node]

    def buildGraph(self, node_list: list[list[int]]) -> Node | None:
        if not node_list:
            return None

        indexed_nodes = {}

        def dfs(index):
            if index in indexed_nodes:
                return indexed_nodes[index]

            node = Node(index + 1)
            indexed_nodes[index] = node

            for value in node_list[index]:
                node.neighbors.append(dfs(value - 1))

            return node

        return dfs(0)

    def areSame(self, node1: Node, node2: Node) -> bool:
        return node1 == node2

    def areEqual(self, node1: Node, node2: Node) -> bool:
        is_node_equal = {}

        def dfs(node1, node2):
            if node1.val in is_node_equal:
                return True
            elif len(node1.neighbors) != len(node2.neighbors):
                return False

            for index in range(len(node1.neighbors)):
                if node1.neighbors[index].val != node2.neighbors[index].val:
                    return False
            
            is_node_equal[node1.val] = True

            return all(dfs(node1, node2)
                       for node1, node2
                       in zip(node1.neighbors, node2.neighbors))

        return dfs(node1, node2)


print(Solution().cloneGraph(Solution().buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]])))
print(Solution().cloneGraph(Solution().buildGraph([[]])))
print(Solution().cloneGraph(Solution().buildGraph([])))

solution = Solution()
graph = solution.buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
cloned_graph = solution.cloneGraph(graph)
print(solution.areSame(graph, graph))
print(solution.areSame(graph, cloned_graph))
print(solution.areEqual(graph, cloned_graph))