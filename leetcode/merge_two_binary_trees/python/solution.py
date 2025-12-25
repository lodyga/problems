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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return None
            elif node1 is None or node2 is None:
                return node1 or node2

            node = TreeNode(node1.val + node2.val)
            node.left = dfs(node1.left, node2.left)
            node.right = dfs(node1.right, node2.right)
            return node

        return dfs(root1, root2)


print(is_same_tree(Solution().mergeTrees(build_tree([1]), build_tree([1, 2])), build_tree([2, 2])))
print(is_same_tree(Solution().mergeTrees(build_tree([1, 3, 2, 5]), build_tree([2, 1, 3, None, 4, None, 7])), build_tree([3, 4, 5, 5, 4, None, 7])))
