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
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
            side effect
        """
        counter = 0

        def dfs(node, prev_max):
            nonlocal counter
            if node is None:
                return

            counter += 1 if node.val >= prev_max else 0
            prev_max = max(prev_max, node.val)
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)

        dfs(root, root.val)
        return counter

    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
            pure function
        """
        def dfs(node, prev_max):
            if node is None:
                return 0

            prev_max = max(prev_max, node.val)
            is_good = True if node.val >= prev_max else False
            left = dfs(node.left, prev_max)
            right = dfs(node.right, prev_max)
            return is_good + left + right

        return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        stack = [(root, root.val)]
        counter = 0

        while stack:
            node, prev_max = stack.pop()
            prev_max = max(prev_max, node.val)
            counter += 1 if node.val >= prev_max else 0

            if node.left:
                stack.append((node.left, prev_max))
            if node.right:
                stack.append((node.right, prev_max))

        return counter

    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        queue = deque([(root, root.val)])
        counter = 0

        while queue:
            node, prev_max = queue.pop()
            prev_max = max(prev_max, node.val)
            counter += 1 if node.val >= prev_max else 0

            if node.left:
                queue.append((node.left, prev_max))
            if node.right:
                queue.append((node.right, prev_max))

        return counter


print(Solution().goodNodes(build_tree([1])) == 1)
print(Solution().goodNodes(build_tree([1, 2, 3])) == 3)
print(Solution().goodNodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4)
print(Solution().goodNodes(build_tree([3, 3, None, 4, 2])) == 3)
