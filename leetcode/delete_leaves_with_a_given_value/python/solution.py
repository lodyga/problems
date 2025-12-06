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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return
            
            node.left = self.removeLeafNodes(node.left, target)
            node.right = self.removeLeafNodes(node.right, target)
            
            if (
                node.val == target and 
                not node.left and 
                not node.right
            ):
                return
            else:
                return node
        
        return dfs(root)


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return
            
            node.left = self.removeLeafNodes(node.left, target)
            node.right = self.removeLeafNodes(node.right, target)
            
            if (
                node.val != target or 
                node.left or 
                node.right
            ):
                return node
            else:
                return
        
        return dfs(root)


print(get_tree_values(Solution().removeLeafNodes(build_tree([2]), 2)) == [])
print(get_tree_values(Solution().removeLeafNodes(build_tree([3]), 2)) == [3])
print(get_tree_values(Solution().removeLeafNodes(build_tree([3, 1, 2]), 2)) == [3, 1])
print(get_tree_values(Solution().removeLeafNodes(build_tree([3, 2, 1]), 2)) == [3, None, 1])
print(get_tree_values(Solution().removeLeafNodes(build_tree([2, 2, 2]), 2)) == [])
print(get_tree_values(Solution().removeLeafNodes(build_tree([1, 2, 3, 2, None, 2, 4]), 2)) , [1, None, 3, None, 4])
print(get_tree_values(Solution().removeLeafNodes(build_tree([1, 3, 3, 3, 2]), 3)) == [1, 3, None, None, 2])
print(get_tree_values(Solution().removeLeafNodes(build_tree([1, 2, None, 2, None, 2]), 2)) == [1])