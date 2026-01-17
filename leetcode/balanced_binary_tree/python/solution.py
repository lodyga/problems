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
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        is_balanced = True

        def dfs(node):
            nonlocal is_balanced
            if node is None:
                return 0
        
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                is_balanced = False

            return 1 + max(left, right)

        dfs(root)
        return is_balanced


print(Solution().isBalanced(build_tree([3])) == True)
print(Solution().isBalanced(build_tree([1, 2, 3])) == True)
print(Solution().isBalanced(build_tree([3, 9, 20, None, None, 15, 7])) == True)
print(Solution().isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) == False)
print(Solution().isBalanced(build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == False)
print(Solution().isBalanced(build_tree([])) == True)
