"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        vals = []

        def dfs(node):
            if node is None:
                return

            for child in node.children:
                dfs(child)
            vals.append(node.val)
        
        dfs(root)
        return vals


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, iteration, post-order traversal
        """
        if not root:
            return []
        
        vals = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if visited:
                vals.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return vals