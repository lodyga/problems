from binary_tree_utils import *


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        values = []

        def dfs(node):
            if not node:
                return
        
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        values = []
        stack = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                values.append(node.val)
                node = node.right
        
        return values


print(Solution().inorderTraversal(build_tree([])), [])
print(Solution().inorderTraversal(build_tree([1])), [1])
print(Solution().inorderTraversal(build_tree([1, None, 2, 3])), [1, 3, 2])
print(Solution().inorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])), [4, 2, 6, 5, 7, 1, 3, 9, 8])