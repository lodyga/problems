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
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree
        """
        def dfs(node1, node2):
            if node1 is None or node2 is None:
                return node1 is None and node2 is None
            elif node1.val != node2.val:
                return False
            
            no_flip = (
                dfs(node1.left, node2.left) and
                dfs(node1.right, node2.right)
            )
            flip = (
                dfs(node1.left, node2.right) and
                dfs(node1.right, node2.left)
            )
            return no_flip or flip
        
        return dfs(root1, root2)


print(Solution().flipEquiv(build_tree([1]), build_tree([1])) == True)
print(Solution().flipEquiv(build_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]), build_tree([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])) == True)
print(Solution().flipEquiv(build_tree([]), build_tree([])) == True)
print(Solution().flipEquiv(build_tree([]), build_tree([1])) == False)