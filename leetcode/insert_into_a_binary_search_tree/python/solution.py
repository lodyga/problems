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
        Tags: linked list, dfs, recursion
        """
        def dfs(node):
            if not node:
                node = TreeNode(val)
            elif node.val < val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            return node
        return dfs(root)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, bfs, iteration
        """
        if not root:
            return TreeNode(val)
        
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


print(get_tree_values(Solution().insertIntoBST(build_tree([]), 5)) == [5])
print(get_tree_values(Solution().insertIntoBST(build_tree([5]), 6)) == [5, None, 6])
print(get_tree_values(Solution().insertIntoBST(build_tree([4, 2, 7, 1, 3]), 5)) == [4, 2, 7, 1, 3, 5])
print(get_tree_values(Solution().insertIntoBST(build_tree([40, 20, 60, 10, 30, 50, 70]), 25)) == [40, 20, 60, 10, 30, 50, 70, None, None, 25])
print(get_tree_values(Solution().insertIntoBST(build_tree([4, 2, 7, 1, 3, None, None, None, None, None, None]), 5)) == [4, 2, 7, 1, 3, 5])