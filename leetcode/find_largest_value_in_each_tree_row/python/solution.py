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
    def largestValues(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue, level order traversal
        """
        values = []

        def bfs(node):
            queue = deque()
            if node:
                queue.append(node)

            while queue:
                for index, _ in enumerate(range(len(queue))):
                    node = queue.popleft()
                    if index == 0:
                        values.append(node.val)
                    elif node.val > values[-1]:
                        values[-1] = node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        bfs(root)
        return values


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, level order traversal
        """
        values = []

        def dfs(index, node):
            if node is None:
                return
            elif len(values) == index:
                values.append(node.val)
            elif node.val > values[index]:
                values[index] = node.val

            dfs(index + 1, node.left)
            dfs(index + 1, node.right)

        dfs(0, root)
        return values


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        values = []
        stack = []

        def dfs(node):
            if root:
                stack.append((0, node))

            while stack:
                index, node = stack.pop()

                if index == len(values):
                    values.append(node.val)
                elif node.val > values[index]:
                    values[index] = node.val
                
                if node.right:
                    stack.append((index + 1, node.right))
                if node.left:
                    stack.append((index + 1, node.left))

        dfs(root)
        return values


print(Solution().largestValues(build_tree([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9])
print(Solution().largestValues(build_tree([1, 2, 3])) == [1, 3])
print(Solution().largestValues(build_tree([])) == [])
print(Solution().largestValues(build_tree([3, 1, 5, 0, 2, 4, 6])) == [3, 5, 6])