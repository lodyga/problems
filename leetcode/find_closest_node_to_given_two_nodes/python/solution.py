from collections import deque


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bfs, iteration, graph
        """
        if node1 == node2:
            return node1

        def bfs(node):
            node_map = {}  # {node index: distance from root}
            queue = deque([node])
            distance = 0

            while queue:
                node = queue.popleft()
                node_map[node] = distance
                if (
                    edges[node] != -1 and 
                    edges[node] not in node_map
                ):
                    queue.append(edges[node])
                distance += 1
            return node_map

        node1_distances = bfs(node1)
        node2_distances = bfs(node2)

        min_distance = 10**5
        min_node = -1
        for node in node1_distances.keys() & node2_distances.keys():
            distance = max(node1_distances[node], node2_distances[node])
            if (
                distance < min_distance or
                distance == min_distance and node < min_node
            ):
                min_distance = distance
                min_node = node
        return min_node


print(Solution().closestMeetingNode([2, 2, 3, -1], 0, 1) == 2)
print(Solution().closestMeetingNode([1, 2, -1], 0, 2) == 2)
print(Solution().closestMeetingNode([4, 4, 4, 5, 1, 2, 2], 1, 1) == 1)
print(Solution().closestMeetingNode([9, 8, 7, 0, 5, 6, 1, 3, 2, 2], 1, 6) == 1)
print(Solution().closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6) == 1)
