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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        res = 0

        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res


print(Solution().diameterOfBinaryTree(build_tree([5])) == 0)
print(Solution().diameterOfBinaryTree(build_tree([1, 2])) == 1)
print(Solution().diameterOfBinaryTree(build_tree([1, 2, 3])) == 2)
print(Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3)
