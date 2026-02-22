class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, array
            A: DFS
            Model: graph
        """
        if node1 == node2:
            return node1

        UPPER_BOUND = 10**5

        def dfs(node: int, dist_map: dict[int, int], dist: int) -> dict[int, int]:
            if (
                node in dist_map or
                node == -1
            ):
                return

            dist_map[node] = dist
            dfs(edges[node], dist_map, dist + 1)
            return dist_map

        dists1 = dfs(node1, {}, 0)
        dists2 = dfs(node2, {}, 0)
        min_dist = UPPER_BOUND
        res = -1

        for node in range(len(edges)):
            if node in dists1 and node in dists2:
                dist = max(dists1[node], dists2[node])

                if dist < min_dist:
                    min_dist = dist
                    res = node

        return res


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: deque, hash map, array
            A: BFS
            Model: graph
        """
        if node1 == node2:
            return node1

        UPPER_BOUND = 10**5

        def bfs(node):
            # {node index: distance from root}
            dist_map = {}
            deq = deque([node])
            dist = 0

            while deq:
                node = deq.popleft()
                dist_map[node] = dist

                if (
                    edges[node] != -1 and
                    edges[node] not in dist_map
                ):
                    deq.append(edges[node])

                dist += 1
            return dist_map

        dists1 = bfs(node1)
        dists2 = bfs(node2)
        min_dist = UPPER_BOUND
        res = -1

        for node in range(len(edges)):
            if node in dists1 and node in dists2:
                dist = max(dists1[node], dists2[node])

                if dist < min_dist:
                    min_dist = dist
                    res = node

        return res


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, array
            A: graph traversal
            Model: graph
        """
        if node1 == node2:
            return node1

        UPPER_BOUND = 10**5

        def get_dist(node):
            # {node index: distance from root}
            dist_map = {}
            dist = 0

            while (
                node != -1 and
                node not in dist_map
            ):
                dist_map[node] = dist
                dist += 1
                node = edges[node]
            
            return dist_map

        dists1 = get_dist(node1)
        dists2 = get_dist(node2)
        min_dist = UPPER_BOUND
        res = -1

        for node in range(len(edges)):
            if node in dists1 and node in dists2:
                dist = max(dists1[node], dists2[node])

                if dist < min_dist:
                    min_dist = dist
                    res = node

        return res


print(Solution().closestMeetingNode([2, 2, 3, -1], 0, 1) == 2)
print(Solution().closestMeetingNode([1, 2, -1], 0, 2) == 2)
print(Solution().closestMeetingNode([4, 4, 4, 5, 1, 2, 2], 1, 1) == 1)
print(Solution().closestMeetingNode([9, 8, 7, 0, 5, 6, 1, 3, 2, 2], 1, 6) == 1)
print(Solution().closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6) == 1)
print(Solution().closestMeetingNode([5, -1, 3, 4, 5, 6, -1, -1, 4, 3], 0, 0) == 0)
print(Solution().closestMeetingNode([2, 0, 0], 2, 0) == 0)
