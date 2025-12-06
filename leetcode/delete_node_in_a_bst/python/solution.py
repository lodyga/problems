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
        Tags: binary tree
        """
        if not root or root.val is None:
            return root
        
        def dfs(node):
            if node is None:
                return None
            elif key == node.val:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
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
        

print(get_tree_values(Solution().deleteNode(build_tree([5, 3, 6]), 6)) == [5, 3])
print(get_tree_values(Solution().deleteNode(build_tree([5, 3, 6]), 3)) == [5, None, 6])
print(get_tree_values(Solution().deleteNode(build_tree([5, 3, 6]), 5)) == [6, 3])
print(get_tree_values(Solution().deleteNode(build_tree([5, 3, 6, 2, 4, None, 7]), 3)) == [5, 4, 6, 2, None, None, 7])
print(get_tree_values(Solution().deleteNode(build_tree([5, 3, 6, 2, 4, None, 7]), 0)) == [5, 3, 6, 2, 4, None, 7])
print(get_tree_values(Solution().deleteNode(build_tree([]), 0)) == [])
print(get_tree_values(Solution().deleteNode(build_tree([0]), 0)) == [])