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
    def lowestCommonAncestor(self, root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        if root is None:
            return
        elif (
            root.val in (p.val, q.val) or
            p.val < root.val < q.val or
            q.val < root.val < p.val
        ):
            return root
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return


class Solution:
    def lowestCommonAncestor(self, root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            DS: binary tree
            A: dfs, iteration, pre-order traversal
        """
        node = root
        
        while node:
            if max(p.val, q.val) < node.val:
                node = node.left
            elif node.val < min(p.val, q.val):
                node = node.right
            else:  # node in (p, q)
                return node


print(Solution().lowestCommonAncestor(build_tree([2, 1]), build_tree([2]), build_tree([1])).val == 2)
print(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([8])).val == 6)
print(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([4])).val == 2)
print(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([3]), build_tree([5])).val == 4)
