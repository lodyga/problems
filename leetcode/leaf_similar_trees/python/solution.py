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
    def leafSimilar(self, root_1: TreeNode, root_2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        mutable list-passing (side effects)
        """
        def get_tree_leafs(node, leaf_list):
            if not node:
                return
            elif not node.left and not node.right:
                leaf_list.append(node.val)
                return

            get_tree_leafs(node.left, leaf_list)
            get_tree_leafs(node.right, leaf_list)
        
        leaf_list_1 = []
        get_tree_leafs(root_1, leaf_list_1)
        leaf_list_2 = []
        get_tree_leafs(root_2, leaf_list_2)
        return leaf_list_1 == leaf_list_2


class Solution:
    def leafSimilar(self, root_1: TreeNode, root_2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        functional (no side effects), concatenation overhead
        """
        def get_leaf_sequence(node):
            if not node:
                return []
            elif not node.left and not node.right:
                return [node.val]
            return get_leaf_sequence(node.left) + get_leaf_sequence(node.right)
        
        return get_leaf_sequence(root_1) == get_leaf_sequence(root_2)


print(Solution().leafSimilar(build_tree([1, 2]), build_tree([2, 2])) == True)
print(Solution().leafSimilar(build_tree([1, 2, 3]), build_tree([1, 3, 2])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])) == True)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None,None, 9, 11, None, None, 8, 10]), build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10])) == False)