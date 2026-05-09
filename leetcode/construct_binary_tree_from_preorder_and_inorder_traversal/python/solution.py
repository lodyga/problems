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
    def buildTreeFromPreIn(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, in-order traversal, pre-order traversal
        """
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        
        def dfs(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode | None:
            if (
                pre_start > pre_end or
                # Leetcode tests never have None in input.
                pre_start == pre_end and preorder[pre_start] is None
            ):
                return None
            
            val = preorder[pre_start]
            node = TreeNode(val)
            idx = inorder_idx[val] 
            left_subtree_size = idx - in_start
            node.left = dfs(
                pre_start + 1, 
                pre_start + left_subtree_size, 
                in_start, 
                idx - 1
            )
            node.right = dfs(
                pre_start + 1 + left_subtree_size, 
                pre_end, 
                idx + 1, 
                in_end
            )
            return node

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


class Solution:
    def buildTreeFromPreIn(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, in-order traversal, pre-order traversal
        """
        if preorder in ([], [None]):
            return None

        val = preorder[0]
        idx = inorder.index(val)
        node = TreeNode(val)
        node.left = self.buildTreeFromPreIn(
            preorder[1: idx + 1],
            inorder[: idx])
        node.right = self.buildTreeFromPreIn(
            preorder[idx + 1:],
            inorder[idx + 1:])

        return node


print(is_same_tree(Solution().buildTreeFromPreIn([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), build_tree([3, 9, 20, None, None, 15, 7])))
print(is_same_tree(Solution().buildTreeFromPreIn([-1], [-1]), build_tree([-1])))
print(is_same_tree(Solution().buildTreeFromPreIn([], []), build_tree([])))
print(is_same_tree(Solution().buildTreeFromPreIn([1, None, 3], [None, 1, 3]), build_tree([1, None, 3])))
