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
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        self.range_sum = 0

        def dfs(node):
            if not node:
                return 0
            
            if low <= node.val <= high:
                self.range_sum += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return self.range_sum


print(Solution().rangeSumBST(build_tree([10, 5, 15, 3, 7, None, 18]), 7, 15) == 32)
print(Solution().rangeSumBST(build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10) == 23)