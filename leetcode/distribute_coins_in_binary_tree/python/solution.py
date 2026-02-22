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
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        res = 0

        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res += abs(left) + abs(right)
            return (node.val - 1) + left + right

        dfs(root)
        return res


print(Solution().distributeCoins(build_tree([1])) == 0)
print(Solution().distributeCoins(build_tree([2, 0])) == 1)
print(Solution().distributeCoins(build_tree([0, 2])) == 1)
print(Solution().distributeCoins(build_tree([3, 0, 0])) == 2)
print(Solution().distributeCoins(build_tree([0, 3, 0])) == 3)
print(Solution().distributeCoins(build_tree([1, 0, 0, None, 3])) == 4)
print(Solution().distributeCoins(build_tree([4, 0, 0, 0])) == 4)
