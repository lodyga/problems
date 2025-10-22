class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: graph, bucket sort, array
        """
        vertex_degree = [0] * n
        for u, v in roads:
            if u != v:
                vertex_degree[u] += 1
                vertex_degree[v] += 1
        
        buckets = [set() for _ in range(n)]  # {connection count: set(vertex...), ...}
        for vertex, degree in enumerate(vertex_degree):
            buckets[degree].add(vertex)
        
        importance_map = [0] * n  # town index -> importance
        importance_value = n
        for bucket in reversed(buckets):
            if bucket:
                for vertex in bucket:
                    importance_map[vertex] = importance_value
                    importance_value -= 1
        
        total_importance = 0
        for vertex in range(n):
            total_importance += importance_map[vertex] * vertex_degree[vertex]
        
        return total_importance


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: graph, bucket sort, hash map
        """
        vertex_degree = {vertex: 0 for vertex in range(n)}
        for u, v in roads:
            if u != v:
                vertex_degree[u] += 1
                vertex_degree[v] += 1
        
        buckets = {vertex: set() for vertex in range(n)}  # {connection count: set(vertex...), ...}
        for vertex, degree in vertex_degree.items():
            buckets[degree].add(vertex)
        
        importance_map = [0] * n  # town index -> importance
        importance_value = n
        for vertex in reversed(range(1, n)):
            if buckets[vertex]:
                for vertex in buckets[vertex]:
                    importance_map[vertex] = importance_value
                    importance_value -= 1
        
        total_importance = 0
        for u, v in roads:
            total_importance += importance_map[u] + importance_map[v]
        
        return total_importance


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]) == 43)
print(Solution().maximumImportance(5, [[0, 3], [2, 4], [1, 3]]) == 20)
print(Solution().maximumImportance(5, [[0, 1]]) == 9)