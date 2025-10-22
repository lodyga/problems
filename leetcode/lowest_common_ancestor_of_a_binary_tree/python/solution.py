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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node):
            if node is None:
                return 
            elif node in (p, q):  
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right
            
        return dfs(root)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        Compare node values, not nodes themselves.
        """
        def dfs(node):
            if node is None:
                return
            elif node.val in (p.val, q.val):
                return node.val

            left = dfs(node.left)
            right = dfs(node.right)
  
            if left and right:
                return node.val
            
            return left or right

        return dfs(root)
    


print(Solution().lowestCommonAncestor(build_tree([2, 1]), build_tree([2]), build_tree([1])), 2)
print(Solution().lowestCommonAncestor(build_tree([3,5,1,6,2,0,8,None,None,7,4]), build_tree([5]), build_tree([1])), 3)
print(Solution().lowestCommonAncestor(build_tree([3,5,1,6,2,0,8,None,None,7,4]), build_tree([6]), build_tree([2])), 5)
print(Solution().lowestCommonAncestor(build_tree([3,5,1,6,2,0,8,None,None,7,4]), build_tree([5]), build_tree([4])), 5)