from binary_tree_utils import *
from collections import deque


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return 

            node.left, node.right = node.right, node.left
            dfs(node.right)
            dfs(node.left)
        
        dfs(root)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return 

            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left
        
        dfs(root)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        if root is None:
            return
        
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        if root is None:
            return
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return root


print(get_tree_values(Solution().invertTree(build_tree([2, 1, 3]))) == [2, 3, 1])
print(get_tree_values(Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1])
print(get_tree_values(Solution().invertTree(build_tree([7, 3, 15, None, None, 9, 20]))) == [7, 15, 3, 20, 9])
print(get_tree_values(Solution().invertTree(build_tree([]))) == [])
