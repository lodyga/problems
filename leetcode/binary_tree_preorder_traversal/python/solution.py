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
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        res = []

        def dfs(node):
            if node is None:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        res = []
        stack = [root] if root else []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        res = []
        stack = []
        node = root
        
        while stack or node:
            if node:
                res.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                # Backtrack to the last right child.
                node = stack.pop()

        return res


print(Solution().preorderTraversal(build_tree([1, None, 2, 3])) == [1, 2, 3])
print(Solution().preorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [1, 2, 4, 5, 6, 7, 3, 8, 9])
print(Solution().preorderTraversal(build_tree([])) == [])
print(Solution().preorderTraversal(build_tree([1])) == [1])
