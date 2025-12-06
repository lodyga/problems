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
    def tree2str(self, root: TreeNode) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        values = []

        def dfs(node):
            if node is None:
                return

            values.append(str(node.val))
            if node.left or node.right:
                values.append("(")
                dfs(node.left)
                values.append(")")
            if node.right:
                values.append("(")
                dfs(node.right)
                values.append(")")

        dfs(root)
        return "".join(values)


print(Solution().tree2str(build_tree([1])) == "1")
print(Solution().tree2str(build_tree([1, 2, 3, 4])) == "1(2(4))(3)")
print(Solution().tree2str(build_tree([1, 2, 3, None, 4])) == "1(2()(4))(3)")