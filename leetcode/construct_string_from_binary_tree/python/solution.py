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
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        parts = []

        def dfs(node):
            if node is None:
                return

            parts.append(str(node.val))

            if node.left or node.right:
                parts.append("(")
                dfs(node.left)
                parts.append(")")

            if node.right:
                parts.append("(")
                dfs(node.right)
                parts.append(")")

        dfs(root)
        return "".join(parts)


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return ""

            res = str(node.val)

            if node.left or node.right:
                res += "(" + dfs(node.left) + ")"

            if node.right:
                res += "(" + dfs(node.right) + ")"

            return res

        return dfs(root)


print(Solution().tree2str(build_tree([1])) == "1")
print(Solution().tree2str(build_tree([1, 2])) == "1(2)")
print(Solution().tree2str(build_tree([1, None, 3])) == "1()(3)")
print(Solution().tree2str(build_tree([1, 2, 3])) == "1(2)(3)")
print(Solution().tree2str(build_tree([1, 2, 3, 4])) == "1(2(4))(3)")
print(Solution().tree2str(build_tree([1, 2, 3, None, 4])) == "1(2()(4))(3)")
