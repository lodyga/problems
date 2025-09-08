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
    def isSubtree(self, root_1: TreeNode | None, root_2: TreeNode | None) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root_2:
            return True
        elif not root_1:
            return False
        elif self.is_same_tree(root_1, root_2):
            return True
        
        return (self.isSubtree(root_1.left, root_2) or 
                self.isSubtree(root_1.right, root_2))
    
    def is_same_tree(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        elif (not root_1 or 
              not root_2 or
              root_1.val != root_2.val):
            return False
        
        return (self.is_same_tree(root_1.left, root_2.left) and
                self.is_same_tree(root_1.right, root_2.right))


print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])), True)
print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])), False)