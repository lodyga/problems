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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: binary tree, dfs, iteration
        """
        node = root
        while root:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: binary tree, dfs, recursion
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


print((Solution().lowestCommonAncestor(build_tree([2, 1]), build_tree([2]), build_tree([1]))).val ==  2)
print((Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([8]))).val == 6)
print((Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([4]))).val == 2)
print((Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([3]), build_tree([5]))).val == 4)