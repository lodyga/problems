class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: backtracking, dfs, recursion
        """
        if edges == [] or edges == [[]]:
            return True
        
        visited = set()
        tree = {}

        for parent, child in edges:
            if parent not in tree:
                tree[parent] = set()
            tree[parent].add(child)

            if child not in tree:
                tree[child] = set()
            tree[child].add(parent)

        def dfs(parent, prev_node):
            # visit every node only once
            if parent in visited:
                return False
            visited.add(parent)
            
            for child in tree[parent]:
                # exclude child -> parend backtracking
                if child == prev_node:
                    continue
                elif not dfs(child, parent):
                    return False        
            
            return True

        # no cycles and connected
        return dfs(0, -1) and len(visited) == n


print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False)
print(Solution().validTree(4, [[0, 1], [2, 3]]) == False)
print(Solution().validTree(5, [[0, 1], [2, 0], [3, 0], [1, 4]]) == True)
print(Solution().validTree(5, [[0, 1], [1, 3], [3, 2], [1, 4]]) == True)
print(Solution().validTree(1, []) == True)