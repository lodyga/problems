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
    def evaluateTree(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return False
            elif node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)


print(Solution().evaluateTree(build_tree([0])) == False)
print(Solution().evaluateTree(build_tree([1])) == True)
print(Solution().evaluateTree(build_tree([2])) == False)
print(Solution().evaluateTree(build_tree([2, 1, 3, None, None, 0, 1])) == True)
