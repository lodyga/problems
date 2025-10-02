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
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        values = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)
            values.append(node.val)
        
        dfs(root)
        return values


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, post-order traversal
        """
        if not root:
            return []
        
        values = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if visited:
                values.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return values