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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal, iteration
        """
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return None

            elif key == node.val:
                if node.left is None or node.right is None:
                    return node.left or node.right

                left_branch = node.left
                right_branch = node.right
                prev = node
                # Node is a new head.
                node = node.right
                # Traverse to new head min value.
                while node.left:
                    prev = node
                    node = node.left

                # Prevent self parent-child loop
                # when prev is node to remove.
                if prev.val != key:
                    prev.left = node.right
                    node.right = right_branch
                node.left = left_branch

            elif key < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)

            return node

        return dfs(root)


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal, iteration
        """
        def dfs(node):
            if node is None:
                return node
            
            elif key == node.val:
                if node.left is None or node.right is None:
                    return node.left or node.right
                else:
                    bottom_node = node.right
                    while bottom_node.left:
                        bottom_node = bottom_node.left
                    node.val = bottom_node.val
                    node.right = self.deleteNode(node.right, node.val)
            elif key < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            
            return node

        return dfs(root)
        

print(is_same_tree(Solution().deleteNode(build_tree([5, 3, 6]), 6), build_tree([5, 3])))
print(is_same_tree(Solution().deleteNode(build_tree([5, 3, 6]), 3), build_tree([5, None, 6])))
print(is_same_tree(Solution().deleteNode(build_tree([5, 3, 6]), 5), build_tree([6, 3])))
print(is_same_tree(Solution().deleteNode(build_tree([5, 3, 6, 2, 4, None, 7]), 3), build_tree([5, 4, 6, 2, None, None, 7])))
print(is_same_tree(Solution().deleteNode(build_tree([5, 3, 6, 2, 4, None, 7]), 0), build_tree([5, 3, 6, 2, 4, None, 7])))
print(is_same_tree(Solution().deleteNode(build_tree([]), 0), build_tree([])))
print(is_same_tree(Solution().deleteNode(build_tree([0]), 0), build_tree([])))
