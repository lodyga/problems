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
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node: TreeNode, lower_bound: int, upper_bound: int) -> bool:
            if node is None:
                return True

            elif (not lower_bound < node.val < upper_bound):
                return False

            left = dfs(node.left, lower_bound, node.val)
            right = dfs(node.right, node.val, upper_bound)

            return left & right

        return dfs(root, -2**31 - 1, 2**31)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        from collections import deque
        queue = deque([(root, -(2**31) - 1, 2**31)])

        while queue:
            node, lower_bound, upper_bound = queue.popleft()

            if not (lower_bound < node.val < upper_bound):
                return False

            if node.left:
                queue.append((node.left, lower_bound, node.val))

            if node.right:
                queue.append((node.right, node.val, upper_bound))

        return True
