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
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        if root1 is root2:
            return True
        elif root1 is None or root2 is None:
            return root1 is None and root2 is None
        elif root1.val != root2.val:
            return False
        elif (  # not flipped
            self.flipEquiv(root1.left, root2.left) and
            self.flipEquiv(root1.right, root2.right)
        ):
            return True
        elif (  # flipped
            self.flipEquiv(root1.left, root2.right) and
            self.flipEquiv(root1.right, root2.left)
        ):
            return True
        else:
            return False


print(Solution().flipEquiv(build_tree([1]), build_tree([1])) == True)
print(Solution().flipEquiv(build_tree([1, 2, 3]), build_tree([1, 3, 2])) == True)
print(Solution().flipEquiv(build_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]), build_tree([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])) == True)
print(Solution().flipEquiv(build_tree([]), build_tree([])) == True)
print(Solution().flipEquiv(build_tree([]), build_tree([1])) == False)
