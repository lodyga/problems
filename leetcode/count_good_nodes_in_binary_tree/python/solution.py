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
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
            side effect
        """
        res = 0

        def dfs(node: TreeNode, max_val: int) -> int:
            nonlocal res
            if node is None:
                return 0

            max_val = max(max_val, node.val)
            res += 1 if node.val >= max_val else 0
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
            pure function
        """
        def dfs(node: TreeNode, max_val: int) -> int:
            if node is None:
                return 0

            max_val = max(max_val, node.val)
            is_good = node.val >= max_val
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            return is_good + left + right

        return dfs(root, root.val)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        stack = [(root, root.val)]
        res = 0

        while stack:
            node, max_val = stack.pop()
            max_val = max(max_val, node.val)
            res += 1 if node.val >= max_val else 0

            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))

        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        from collections import deque
        queue = deque([(root, root.val)])
        res = 0

        while queue:
            node, max_val = queue.pop()
            max_val = max(max_val, node.val)
            res += 1 if node.val >= max_val else 0

            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))

        return res


print(Solution().goodNodes(build_tree([1])) == 1)
print(Solution().goodNodes(build_tree([1, 2, 3])) == 3)
print(Solution().goodNodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4)
print(Solution().goodNodes(build_tree([3, 3, None, 4, 2])) == 3)
