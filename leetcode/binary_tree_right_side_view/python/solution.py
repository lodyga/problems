from binary_tree_utils import *
from collections import deque


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        if root is None:
            return []

        right_side_vals = []
        queue = deque([root])

        while queue:
            for index in range(len(queue)):
                node = queue.popleft()
                
                if index == 0:
                    right_side_vals.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return right_side_vals


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, pre-order traversal
        """
        right_side_vals = []

        def dfs(index, node):
            if node is None:
                return 
            
            if index == len(right_side_vals):
                right_side_vals.append(node.val)

            dfs(index + 1, node.right)
            dfs(index + 1, node.left)
            
        dfs(0, root)
        return right_side_vals


print(Solution().rightSideView(build_tree([1, 2, 3])) == [1, 3])
print(Solution().rightSideView(build_tree([1, None, 3])) == [1, 3])
print(Solution().rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4])
print(Solution().rightSideView(build_tree([])) == [])
