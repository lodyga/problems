from binary_tree_utils import *
# import binary_tree_utils as bt


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, in-order traversal
        """
        total = 0

        def dfs(node):
            nonlocal total
            if node is None:
                return None

            dfs(node.right)
            node.val += total
            total = node.val
            dfs(node.left)
            return node

        return dfs(root)


print(is_same_tree(Solution().convertBST(build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])), build_tree([30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])))
print(is_same_tree(Solution().convertBST(build_tree([0, None, 1])), build_tree([1, None, 1])))
print(is_same_tree(Solution().convertBST(build_tree([3, 2, 4, 1])), build_tree([7, 9, 4, 10])))
print(is_same_tree(Solution().convertBST(build_tree([2, 0, 3, -4, 1])), build_tree([5, 6, 3, 2, 6])))
