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
    def evaluateTree(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root:
            return False
        elif root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            return self.evaluateTree(root.left) or \
                self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and \
                self.evaluateTree(root.right)


print(Solution().evaluateTree(build_tree([0])), False)
print(Solution().evaluateTree(build_tree([1])), True)
print(Solution().evaluateTree(build_tree([2])), False)
print(Solution().evaluateTree(build_tree([2, 1, 3, None, None, 0, 1])), True)