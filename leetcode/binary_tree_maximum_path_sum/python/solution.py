from binary_tree_utils import *


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = leftn
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        def dfs(node: TreeNode):
            nonlocal res

            if node is None:
                return 0

            node_left = dfs(node.left)
            node_right = dfs(node.right)

            path_sum = node.val + node_left + node_right
            res = max(res, path_sum)

            return max(node.val + max(node_left, node_right), 0)

        res = root.val
        dfs(root)
        return res


print(Solution().maxPathSum(build_tree([1, 2, 3])) == 6)
print(Solution().maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42)
print(Solution().maxPathSum(build_tree([3])) == 3)
print(Solution().maxPathSum(build_tree([-3])) == -3)
print(Solution().maxPathSum(build_tree([4, 5, 6])) == 15)
print(Solution().maxPathSum(build_tree([4, -5, 6])) == 10)
print(Solution().maxPathSum(build_tree([4, 5, -6])) == 9)
print(Solution().maxPathSum(build_tree([-4, 5, 6])) == 7)
print(Solution().maxPathSum(build_tree([1, -2, -3, 1, 3, -2, None, -1])) == 3)
print(Solution().maxPathSum(build_tree([-15, 10, 20, None, None, 15, 5, -5])) == 40)
