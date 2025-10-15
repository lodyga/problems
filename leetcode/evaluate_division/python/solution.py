class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        """
        Time complexity: O((V + E) * q)
            q: query length
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph
        """
        adjs = {}
        for (src, dst), val in zip(equations, values):
            if src not in adjs:
                adjs[src] = set()
            adjs[src].add((dst, val))
            if dst not in adjs:
                adjs[dst] = set()
            adjs[dst].add((src, 1/val))
        
        visited = set()
        
        def dfs(src, dst):
            if (
                src not in adjs or
                src in visited
            ):
                return -1.0
            elif src == dst:
                return 1

            visited.add(src)
            
            for adj_dst, adj_val in adjs[src]:
                dfs_result = dfs(adj_dst, dst)
                if dfs_result != -1:
                    return dfs_result * adj_val
            
            visited.pop()
            return -1

        return [dfs(src, dst) for src, dst in queries]


from collections import deque


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        """
        Time complexity: O((V + E) * q)
            q: query length
        Auxiliary space complexity: O(V + E)
        Tags: bfs, iteration, graph
        """
        adjs = {}
        for (src, dst), val in zip(equations, values):
            if src not in adjs:
                adjs[src] = set()
            adjs[src].add((dst, val))
            if dst not in adjs:
                adjs[dst] = set()
            adjs[dst].add((src, 1/val))
        
        def bfs(src, dst):
            if (
                src not in adjs or
                dst not in adjs
            ):
                return -1.0
            
            queue = deque([(src, 1)])
            visited = set([src])

            while queue:
                src, weight = queue.popleft()    
                if src == dst:
                    return weight
            
                for dst, adj_weight in adjs[src]:
                    if dst not in visited:
                        queue.append((dst, weight * adj_weight))
                        visited.add(dst)
            
            return -1

        return [bfs(src, dst) for src, dst in queries]


print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]), [6.00000, 0.50000, -1.00000, 1.00000, -1.00000])
print(Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]), [3.75000, 0.40000, 5.00000, 0.20000])
print(Solution().calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]), [0.50000, 2.00000, -1.00000, -1.00000])