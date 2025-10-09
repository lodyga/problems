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


print(Solution().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]), [[0, 0, 1], [3, 0, 0], [0, 2, 0]])
print(Solution().buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]), [])