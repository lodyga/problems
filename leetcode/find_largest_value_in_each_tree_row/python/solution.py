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
        Tags:
            DS: binary tree, queue, list
            A: bfs, iteration, level-order traversal
        """
        res = []

        def bfs(node):
            queue = deque()
            if node:
                queue.append(node)

            while queue:
                res.append(queue[0].val)

                for _ in range(len(queue)):
                    node = queue.popleft()
                    res[-1] = max(res[-1], node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        bfs(root)
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, level-order traversal
        """
        res = []

        def dfs(index, node):
            if node is None:
                return
            elif len(res) == index:
                res.append(node.val)
            elif node.val > res[index]:
                res[index] = node.val

            dfs(index + 1, node.left)
            dfs(index + 1, node.right)

        dfs(0, root)
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list, stack
            A: dfs, iteration, level-order traversal
        """
        res = []
        stack = []

        def dfs(node):
            if root:
                stack.append((0, node))

            while stack:
                index, node = stack.pop()

                if index == len(res):
                    res.append(node.val)
                elif node.val > res[index]:
                    res[index] = node.val

                if node.right:
                    stack.append((index + 1, node.right))
                if node.left:
                    stack.append((index + 1, node.left))

        dfs(root)
        return res


print(Solution().largestValues(build_tree([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9])
print(Solution().largestValues(build_tree([1, 2, 3])) == [1, 3])
print(Solution().largestValues(build_tree([])) == [])
print(Solution().largestValues(build_tree([3, 1, 5, 0, 2, 4, 6])) == [3, 5, 6])
print(Solution().largestValues(build_tree([34, -6, None, -21])) == [34, -6, -21])
