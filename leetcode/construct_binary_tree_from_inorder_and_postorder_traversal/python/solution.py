import binary_tree_utils as bt


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> bt.TreeNode:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, in-order traversal, post-order traversal
        """
        if postorder == [] or postorder == [None]:
            return None

        node_value = postorder[-1]
        node_index = inorder.index(node_value)
        node = bt.TreeNode(node_value)
        node.left = self.buildTree(
            inorder[: node_index],
            postorder[: node_index])
        node.right = self.buildTree(
            inorder[node_index + 1: ],
            postorder[node_index: -1])
        return node


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> bt.TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, in-order traversal, post-order traversal
        """
        inorder_index = {value: index 
                         for index, value in enumerate(inorder)}

        def dfs(in_start, in_end, post_start, post_end):
            if (
                in_start > in_end or
                post_start > post_end or
                # Leetcode tests never have None in input.
                in_start == in_end and postorder[in_start] is None
            ):
                return None

            node_value = postorder[post_end]
            node_index = inorder_index[node_value]
            left_subtree_size = node_index - in_start
            node = bt.TreeNode(node_value)
            node.left = dfs(
                in_start, node_index - 1,
                post_start, post_start + left_subtree_size - 1)
            node.right = dfs(
                node_index + 1, in_end,
                post_start + left_subtree_size, post_end - 1)
            return node

        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)


print(bt.is_same_tree(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), bt.build_tree([3, 9, 20, None, None, 15, 7])))
print(bt.is_same_tree(Solution().buildTree([-1], [-1]), bt.build_tree([-1])))
print(bt.is_same_tree(Solution().buildTree([], []), bt.build_tree([])))
print(bt.is_same_tree(Solution().buildTree([None, 1, 3], [None, 3, 1]), bt.build_tree([1, None, 3])))