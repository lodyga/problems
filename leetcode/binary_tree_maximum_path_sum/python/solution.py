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
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        max_path_sum = root.val

        def dfs(node):
            nonlocal max_path_sum
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            path_sum = node.val + left + right
            max_path_sum = max(max_path_sum, path_sum)

            return max(0, node.val + max(left, right))

        dfs(root)
        return max_path_sum


print(Solution().maxPathSum(build_tree([3])) == 3)
print(Solution().maxPathSum(build_tree([-3])) == -3)
print(Solution().maxPathSum(build_tree([4, 5, 6])) == 15)
print(Solution().maxPathSum(build_tree([1, 2, 3])) == 6)
print(Solution().maxPathSum(build_tree([4, -5, 6])) == 10)
print(Solution().maxPathSum(build_tree([4, 5, -6])) == 9)
print(Solution().maxPathSum(build_tree([-4, 5, 6])) == 7)
print(Solution().maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42)
print(Solution().maxPathSum(build_tree([1, -2, -3, 1, 3, -2, None, -1])) == 3)
print(Solution().maxPathSum(build_tree([-15, 10, 20, None, None, 15, 5, -5])) == 40)
