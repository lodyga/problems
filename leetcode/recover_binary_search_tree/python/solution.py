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
    def recoverTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, in-order traversal
        """
        vals = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            vals.append(node)
            inorder(node.right)

        inorder(root)
        node1 = None
        node2 = None
        
        for index in range(len(vals) - 1):
            if vals[index].val > vals[index + 1].val:
                node2 = vals[index + 1]
            
                if node1:
                    break
                    
                node1 = vals[index]
                
        node1.val, node2.val = node2.val, node1.val

        return root

# 3, 2, 1
print(is_same_tree(Solution().recoverTree(build_tree([1, 3, None, None, 2])), build_tree([3, 1, None, None, 2])))
print(is_same_tree(Solution().recoverTree(build_tree([3, 1, 4, None, None, 2])), build_tree([2, 1, 4, None, None, 3])))
