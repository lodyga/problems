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
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree
        """
        self.min_diff = 10**5 + 1
        self.prev_node = None

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            if self.prev_node:
                self.min_diff = min(self.min_diff, node.val - self.prev_node.val)
            self.prev_node = node
            dfs(node.right)

        dfs(root)
        return self.min_diff


print(Solution().minDiffInBST(build_tree([3, None, 6])) == 3)
print(Solution().minDiffInBST(build_tree([4, 2, 6, 1, 3])) == 1)
print(Solution().minDiffInBST(build_tree([1, 0, 48, None, None, 12, 49])) == 1)
print(Solution().minDiffInBST(build_tree([90, 69, None, 49, 89, None, 52])) == 1)
print(Solution().minDiffInBST(build_tree([41, 19, 62, 11, 31, None, 89, 8, 18, None, None, 74, None, None, None, 16])) == 1)