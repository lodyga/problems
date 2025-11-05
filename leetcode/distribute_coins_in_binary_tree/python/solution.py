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
    def distributeCoins(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        distribution_count = 0

        def dfs(node):
            nonlocal distribution_count
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            distribution_count += abs(left) + abs(right)
            coins_surplus = node.val + left + right - 1
            # distribution_count += abs(coins_surplus)
            return coins_surplus

        dfs(root)
        return distribution_count


print(Solution().distributeCoins(build_tree([3, 0, 0])) == 2)
print(Solution().distributeCoins(build_tree([0, 3, 0])) == 3)
print(Solution().distributeCoins(build_tree([1, 0, 0, None, 3])) == 4)
