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
    def postorderTraversal(self, root: TreeNode) -> list[int]:
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
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
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

        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node.left)
                node = node.right
            else:
                node = stack.pop()

        res.reverse()
        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
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

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        res.reverse()
        return res


print(Solution().postorderTraversal(build_tree([1, None, 2, 3])) == [3, 2, 1])
print(Solution().postorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [4, 6, 7, 5, 2, 9, 8, 3, 1])
print(Solution().postorderTraversal(build_tree([])) == [])
print(Solution().postorderTraversal(build_tree([1])) == [1])
