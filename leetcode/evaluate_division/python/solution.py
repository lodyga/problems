class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        """
        Time complexity: O((V + E) * q)
            q: query length
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: DFS
            Model: graph
        """
        adjs = {}
        for (src, dst), val in zip(equations, values):
            if src not in adjs:
                adjs[src] = []
            adjs[src].append((dst, val))
            if dst not in adjs:
                adjs[dst] = []
            adjs[dst].append((src, 1/val))
        
        def dfs(src, dst, visited):
            if (
                src not in adjs or
                src in visited
            ):
                return -1
            elif src == dst:
                return 1

            visited.add(src)
            
            for adj_dst, adj_val in adjs[src]:
                res = dfs(adj_dst, dst, visited)
                if res != -1:
                    return res * adj_val
            
            return -1

        return [dfs(src, dst, set()) for src, dst in queries]


print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000])
print(Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000, 5.00000, 0.20000])
print(Solution().calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [0.50000, 2.00000, -1.00000, -1.00000])
