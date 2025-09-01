class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        ROWS = len(is_connected)
        COLS = len(is_connected[0])
        rank = [1] * ROWS
        parents = list(range(ROWS))
        province_count = ROWS

        def find(vertex):
            while vertex != parents[vertex]:
                parents[vertex] = parents[parents[vertex]]
                vertex = parents[vertex]
            return vertex
        
        def union(vertex1, vertex2):
            parent1 = find(vertex1)
            parent2 = find(vertex2)
            
            if parent1 == parent2:
                return 0
            elif rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            return 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if row != col and is_connected[row][col]:
                    province_count -= union(row, col)

        return province_count


class Solution2:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DFS
        """
        ROWS = len(is_connected)
        COLS = len(is_connected[0])
        adj = {province: set() for province in range(ROWS)}
        province_count = 0
        visited = [False] * ROWS

        for row in range(ROWS):
            for col in range(COLS):
                if row != col and is_connected[row][col]:
                    adj[row].add(col)

        def dfs(province):
            if visited[province]:
                return

            visited[province] = True
            
            for adj_province in adj[province]:
                dfs(adj_province)
            
        for province in adj:
            if not visited[province]:
                dfs(province)
                province_count += 1
        
        return province_count


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)