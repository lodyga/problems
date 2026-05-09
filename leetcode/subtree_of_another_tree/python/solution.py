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
    def isSubtree(self, root: TreeNode | None, sub_root: TreeNode) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def _is_same_tree(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if (node1 is None and node2 is None):
                return True
            elif (
                node1 is None or node2 is None or
                node1.val != node2.val
            ):
                return False
            
            left = _is_same_tree(node1.left, node2.left)
            right = _is_same_tree(node1.right, node2.right)

            return left and right

        if sub_root is None:
            return True
        elif root is None:
            return False
        elif _is_same_tree(root, sub_root):
            return True

        left = self.isSubtree(root.left, sub_root)
        right = self.isSubtree(root.right, sub_root)

        return left or right


print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])) == True)
print(Solution().isSubtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])) == False)
print(Solution().isSubtree(build_tree([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]), build_tree([1, None, 1, None, 1, None, 1, None, 1, None, 1, 2])) == True)
