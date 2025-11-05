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
    def isSubtree(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def is_same_tree(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            
            return (
                is_same_tree(root1.left, root2.left) and
                is_same_tree(root1.right, root2.right)
            )
        
        if root2 is None:
            return True
        elif root1 is None:
            return False
        elif is_same_tree(root1, root2):
            return True
            
        return (
            self.isSubtree(root1.left, root2) or
            self.isSubtree(root1.right, root2)
        )


print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])) == True)
print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])) == False)