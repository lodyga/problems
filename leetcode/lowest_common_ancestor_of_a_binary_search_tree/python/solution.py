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
        Auxiliary space complexity: O(logn)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return
            elif (
                p.val < node.val < q.val or
                q.val < node.val < p.val
            ):
                return node
            elif (
                node.val > p.val and
                node.val > q.val
            ):
                return dfs(node.left)
            elif (
                node.val < p.val and
                node.val < q.val
            ):
                return dfs(node.right)
            else:  # node in (p, q)
                return node

        return dfs(root)
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: binary tree
            A: dfs, iteration, pre-order traversal
        """
        node = root
        while node:
            if (
                node.val > p.val and 
                node.val > q.val
            ):
                node = node.left
            elif (
                node.val < p.val and 
                node.val < q.val
            ):
                node = node.right
            else:  # node in (p, q)
                return node


print(get_tree_values(Solution().lowestCommonAncestor(build_tree([2, 1]), build_tree([2]), build_tree([1])))[0] == 2)
print(get_tree_values(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([8])))[0] == 6)
print(get_tree_values(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([2]), build_tree([4])))[0] == 2)
print(get_tree_values(Solution().lowestCommonAncestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), build_tree([3]), build_tree([5])))[0] == 4)
