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
    def rob(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node):
            if node is None:
                return (0, 0)

            node_left = dfs(node.left)
            node_right = dfs(node.right)
            with_node = node.val + node_left[1] + node_right[1]
            without_node = max(node_left) + max(node_right)

            return (with_node, without_node)

        return max(dfs(root))


print(Solution().rob(build_tree([3, 2, 3, None, 3, None, 1])) == 7)
print(Solution().rob(build_tree([3, 4, 5, 1, 3, None, 1])) == 9)
print(Solution().rob(build_tree([4, 1, None, 2, None, 3])) == 7)
print(Solution().rob(build_tree([79, 99, 77, None, None, None, 69, None, 60, 53, None, 73, 11, None, None, None, 62, 27, 62, None, None, 98, 50, None, None, 90, 48, 82, None, None, None, 55, 64, None, None, 73, 56, 6, 47, None, 93, None, None, 75, 44, 30, 82, None, None, None, None, None, None, 57, 36, 89, 42, None, None, 76, 10, None, None, None, None, None, 32, 4, 18, None, None, 1, 7, None, None, 42, 64, None, None, 39, 76, None, None, 6, None, 66, 8, 96, 91, 38, 38, None, None, None, None, 74, 42, None, None, None, 10, 40, 5, None, None, None, None, 28, 8, 24, 47, None, None, None, 17, 36, 50, 19, 63, 33, 89, None, None, None, None, None, None, None, None, 94, 72, None, None, 79, 25, None, None, 51, None, 70, 84, 43, None, 64, 35, None, None, None, None, 40, 78, None, None, 35, 42, 98, 96, None, None, 82, 26, None, None, None, None, 48, 91, None, None, 35, 93, 86, 42, None, None, None, None, 0, 61, None, None, 67, None, 53, 48, None, None, 82, 30, None, 97, None, None, None, 1, None, None])) == 3038)