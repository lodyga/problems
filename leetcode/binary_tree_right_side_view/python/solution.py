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
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue, level order traversal
        """
        queue = deque([root])
        right_side_view = []

        while queue:
            level_view = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if level_view is None:
                        level_view = node.val
                    queue.append(node.right)
                    queue.append(node.left)
            
            if level_view:
                right_side_view.append(level_view)
        
        return right_side_view


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, level order traversal
        """
        right_side_view = []

        def dfs(index, node):
            if not node:
                return
            elif index == len(right_side_view):
                right_side_view.append(node.val)
            
            dfs(index + 1, node.right)
            dfs(index + 1, node.left)
        
        dfs(0, root)
        return right_side_view


print(Solution().rightSideView(build_tree([1, 2, 3])), [1, 3])
print(Solution().rightSideView(build_tree([1, None, 3])), [1, 3])
print(Solution().rightSideView(build_tree([1, 2, 3, None, 5, None, 4])), [1, 3, 4])
print(Solution().rightSideView(build_tree([])), [])