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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        node_list = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            node_list.append(node.val)

        dfs(root)
        return node_list


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        node_list = []
        stack = []
        node = root

        while node or stack:
            if node:
                node_list.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left

        node_list.reverse()
        return node_list


print(Solution().postorderTraversal(build_tree([])) == [])
print(Solution().postorderTraversal(build_tree([1])) == [1])
print(Solution().postorderTraversal(build_tree([1, None, 2, 3])) == [3, 2, 1])
print(Solution().postorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [4, 6, 7, 5, 2, 9, 8, 3, 1])