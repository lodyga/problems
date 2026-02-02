class Solution:
    def buildMatrix(self, k: int, row_conds: list[list[int]], col_conds: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(k2)
        Auxiliary space complexity: O(k)
        Tags:
            DS: array (matrix)
            A: multi-source DFS, topological sort with cycle detection
            Model: graph
        """
        
        def dfs(col, sorted, visited, prevs):
            if visited[col] != -1:
                return bool(visited[col])
            
            visited[col] = 1

            for prev_col in prevs[col]:
                if dfs(prev_col, sorted, visited, prevs):
                    return True

            sorted.append(col)
            visited[col] = 0
            return False
        
        ROWS = k
        COLS = k
        
        prev_cols = [[] for _ in  range(COLS)]
        for prev_vertex, vertex in col_conds:
            prev_cols[vertex - 1].append(prev_vertex - 1)

        prev_rows = [[] for _ in  range(ROWS)]
        for prev_vertex, vertex in row_conds:
            prev_rows[vertex - 1].append(prev_vertex - 1)
        
        sorted_cols = []
        # -1: not visited, 0: visited, 1: visiting/current path
        visited_cols = [-1] * COLS
        
        for col in range(COLS):
            if dfs(col, sorted_cols, visited_cols, prev_cols):
                return []
        
        sorted_rows = []
        # -1: not visited, 0: visited, 1: visiting/current path
        visited_rows = [-1] * ROWS

        for row in range(ROWS):
            if dfs(row, sorted_rows, visited_rows, prev_rows):
                return []
        
        coords = {v: [] for v in range(k)}
        for row, val in enumerate(sorted_rows):
            coords[val].append(row)
        for col, val in enumerate(sorted_cols):
            coords[val].append(col)

        res = [[0] * COLS for _ in range(ROWS)]
        for val, (y, x) in coords.items():
            res[y][x] = val + 1
        return res


print(Solution().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]) == [[0, 0, 1], [3, 0, 0], [0, 2, 0]])
print(Solution().buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]) == [])


class TopologicalSort:
    def __init__(self, k, conditions):
        self.k = k
        self.prereqs = {vertex: set() for vertex in range(1, k + 1)}
        for u, v in conditions:
            self.prereqs[v].add(u)

    def sort(self) -> list[int | None]:
        def dfs(vertex):
            if path[vertex - 1] is not None:
                return path[vertex - 1]
            path[vertex - 1] = True
            for prev_vertex in self.prereqs[vertex]:
                if dfs(prev_vertex):
                    return True
            path[vertex - 1] = False
            sequence.append(vertex)
            return False
    
        path = [None] * self.k
        sequence = []
        for vertex in self.prereqs:
            if dfs(vertex):
                return []

        return sequence


class Solution:
    def buildMatrix(self, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(k2 + V + E)
        Auxiliary space complexity: O(k + V + E)
        Tags: dfs, recursion, graph, topological sort
        """
        row_sequence = TopologicalSort(k, row_conditions).sort()
        col_sequence = TopologicalSort(k, col_conditions).sort()
        if not row_sequence or not col_sequence:
            return []
        
        matrix = [[0] * k for _ in range(k)]
        values_row = [0] * k
        for row, value in enumerate(row_sequence):
            values_row[value - 1] = row
        
        for col, value in enumerate(col_sequence):
            row = values_row[value - 1]
            matrix[row][col] = value

        return matrix