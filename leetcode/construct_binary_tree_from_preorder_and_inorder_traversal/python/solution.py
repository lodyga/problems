from binary_tree_utils import *


r"""
draft
preorder: [1, None, 3]
inorder: [None, 1, 3]

        1
    /       \
    None    3

preorder: [3, 9, 20, 15, 7]
inorder: [9, 3, 15, 20, 7]

    3:
9,    15, 20, 7

    9:
        3, 15, 20, 7

    20:
9, 3, 15    7

                    3
                /       \
                9       20
                        /\
                    15      7
"""


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, in-order traversal, pre-order traversal
        """
        if preorder in ([], [None]):
            return None

        node_value = preorder[0]
        node_index = inorder.index(node_value)
        node = TreeNode(node_value)
        node.left = self.buildTree(
            preorder[1: node_index + 1],
            inorder[: node_index])
        node.right = self.buildTree(
            preorder[node_index + 1:],
            inorder[node_index + 1:])

        return node


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, in-order traversal, pre-order traversal
        """
        inorder_index = {val: index for index, val in enumerate(inorder)}

        def dfs(pre_start, pre_end, in_start, in_end):
            if (
                pre_start > pre_end or
                # Leetcode tests never have None in input.
                pre_start == pre_end and preorder[pre_start] is None
            ):
                return None

            node_value = preorder[pre_start]
            node_index = inorder_index[node_value]
            left_subtree_size = node_index - in_start
            node = TreeNode(node_value)
            node.left = dfs(
                pre_start + 1, pre_start + left_subtree_size,
                in_start, node_index - 1)
            node.right = dfs(
                pre_start + 1 + left_subtree_size, pre_end,
                node_index + 1, in_end)
            return node

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


print(is_same_tree(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), build_tree([3, 9, 20, None, None, 15, 7])))
print(is_same_tree(Solution().buildTree([-1], [-1]), build_tree([-1])))
print(is_same_tree(Solution().buildTree([], []), build_tree([])))
print(is_same_tree(Solution().buildTree([1, None, 3], [None, 1, 3]), build_tree([1, None, 3])))
