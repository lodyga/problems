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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        Compare node objects, not just nodes values.
        """
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return
            elif node in (p, q):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            else:
                return left or right
        
        return dfs(root)


# Compare node objects
root, lookup = build_tree([4, 5, 6], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[5], lookup[6]) == lookup[4])
root, lookup = build_tree([4, 5], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[4], lookup[5]) == lookup[4])
root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[5], lookup[1]) == lookup[3])
root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[6], lookup[2]) == lookup[5])
root, lookup = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], with_lookup=True)
print(Solution().lowestCommonAncestor(root, lookup[5], lookup[4]) == lookup[5])


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        Compare node values, not nodes objects.
        """
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return
            elif node.val in (p.val, q.val):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            else:
                return left or right
        
        res = dfs(root)
        res.left = None
        res.right = None
        return res


# Compare node values
print(is_same_tree(Solution().lowestCommonAncestor(build_tree([4, 5, 6]), build_tree([5]), build_tree([6])), build_tree([4])))
print(is_same_tree(Solution().lowestCommonAncestor(build_tree([4, 5]), build_tree([4]), build_tree([5])), build_tree([4])))
print(is_same_tree(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([5]), build_tree([1])), build_tree([3])))
print(is_same_tree(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([6]), build_tree([2])), build_tree([5])))
print(is_same_tree(Solution().lowestCommonAncestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), build_tree([5]), build_tree([4])), build_tree([5])))

