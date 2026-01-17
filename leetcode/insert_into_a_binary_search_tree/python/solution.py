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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return TreeNode(val)
            elif val < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node

        return dfs(root)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: binary tree
            A: dfs, iteration, pre-order traversal
        """
        node = root
        while node:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
        
        return TreeNode(val)


print(is_same_tree(Solution().insertIntoBST(build_tree([]), 5), build_tree([5])))
print(is_same_tree(Solution().insertIntoBST(build_tree([5]), 6), build_tree([5, None, 6])))
print(is_same_tree(Solution().insertIntoBST(build_tree([4, 2, 7, 1, 3]), 5), build_tree([4, 2, 7, 1, 3, 5])))
print(is_same_tree(Solution().insertIntoBST(build_tree([40, 20, 60, 10, 30, 50, 70]), 25), build_tree([40, 20, 60, 10, 30, 50, 70, None, None, 25])))
print(is_same_tree(Solution().insertIntoBST(build_tree([4, 2, 7, 1, 3, None, None, None, None, None, None]), 5), build_tree([4, 2, 7, 1, 3, 5])))
