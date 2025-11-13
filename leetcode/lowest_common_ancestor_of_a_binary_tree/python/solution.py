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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return
            elif node in (p, q):
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        return dfs(root)


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        Compare node values, not nodes themselves.
        """
        def dfs(node):
            if node is None:
                return
            elif node.val in (p.val, q.val):
                return node.val

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node.val

            return left or right

        return dfs(root)


root, lookup = build_tree([2, 1], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[1], lookup[2]).val == 2)

root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[5], lookup[1]).val == 3)

root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[6], lookup[2]).val == 5)

root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[5], lookup[4]).val == 5)

# print(Solution().lowestCommonAncestor(build_tree([2, 1]), build_tree([2]), build_tree([1])) == 2)
# print(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([5]), build_tree([1])) == 3)
# print(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([6]), build_tree([2])) == 5)
# print(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([5]), build_tree([4])) == 5)
