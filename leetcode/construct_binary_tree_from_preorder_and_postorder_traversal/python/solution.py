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
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, pre-order traversal, post-order traversal
        """
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        
        value = preorder[1]
        index = postorder.index(value)
        left_subtree_size = index + 1
        node.left = self.constructFromPrePost(
            preorder[1: 1 + left_subtree_size],
            postorder[: left_subtree_size]
        )
        if len(preorder) > 2:
            node.right = self.constructFromPrePost(
                preorder[1 + left_subtree_size: ],
                postorder[left_subtree_size: -1]
            )
        return node


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, pre-order traversal, post-order traversal
        """
        postorder_index = {value: index 
                           for index, value in enumerate(postorder)}
        
        def dfs(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            node = TreeNode(preorder[pre_start])
            if pre_end == pre_start:
                return node
        
            value = preorder[pre_start + 1]
            index = postorder_index[value]
            left_subtree_size = index - post_start + 1
            node.left = dfs(
                pre_start + 1, pre_start + left_subtree_size,
                post_start, post_start + left_subtree_size - 1
            )
            if pre_end - pre_start > 1:
                node.right = dfs(
                    pre_start + 1 + left_subtree_size, pre_end,
                    index + 1, post_end - 1
            )
            return node
        
        return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)


print(is_same_tree(Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]), build_tree([1, 2, 3, 4, 5, 6, 7])))
print(is_same_tree(Solution().constructFromPrePost([1], [1]), build_tree([1])))
print(is_same_tree(Solution().constructFromPrePost([2, 1], [1, 2]), build_tree([2, 1])))
print(is_same_tree(Solution().constructFromPrePost([2, 1, 3], [3, 1, 2]), build_tree([2, 1, None, 3])))
print(is_same_tree(Solution().constructFromPrePost([3, 9, 20, 15, 7], [9, 15, 7, 20, 3]), build_tree([3, 9, 20, None, None, 15, 7])))