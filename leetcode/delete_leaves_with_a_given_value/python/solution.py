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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if (
                node.val == target and 
                node.left is None and 
                node.right is None
            ):
                return None
            
            return node

        return dfs(root)


print(is_same_tree(Solution().removeLeafNodes(build_tree([2]), 2), build_tree([])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([3]), 2), build_tree([3])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([3, 1, 2]), 2), build_tree([3, 1])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([3, 2, 1]), 2), build_tree([3, None, 1])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([2, 2, 2]), 2), build_tree([])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([1, 3, 3, 3, 2]), 3), build_tree([1, 3, None, None, 2])))
print(is_same_tree(Solution().removeLeafNodes(build_tree([1, 2, None, 2, None, 2]), 2), build_tree([1])))
