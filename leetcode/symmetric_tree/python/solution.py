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
    def isSymmetric(self, root: TreeNode) -> bool | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node1: TreeNode | None, node2: TreeNode | None) -> bool | None:
            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            return (
                node1.val == node2.val and
                dfs(node1.left, node2.right) and
                dfs(node1.right, node2.left)
            )

        return dfs(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, iteration, pre-order traversal
        """
        stack = []
        stack.append((root.left, root.right))

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                continue
            elif (
                left is None or right is None or
                left.val != right.val
            ):
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool | None:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: bfs, iteration, pre-order traversal
        """
        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.popleft()

            if left is None and right is None:
                continue
            elif (
                left is None or right is None or
                left.val != right.val
            ):
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


print(Solution().isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])) == True)
print(Solution().isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])) == False)
