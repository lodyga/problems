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
    def hasPathSum(self, root: TreeNode, target_sum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node, path_sum):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                return path_sum + node.val == target_sum

            left = dfs(node.left, path_sum + node.val)
            right = dfs(node.right, path_sum + node.val)
            return left or right

        return dfs(root, 0)


class Solution:
    def hasPathSum(self, root: TreeNode, target_sum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        if root is None:
            return False

        stack = [(root, 0)]  # [(node, path sum)]

        while stack:
            node, path_sum = stack.pop()
            if (
                node.left is None and
                node.right is None and
                path_sum + node.val == target_sum
            ):
                return True
            if node.right:
                stack.append((node.right, path_sum + node.val))
            if node.left:
                stack.append((node.left, path_sum + node.val))

        return False


class Solution:
    def hasPathSum(self, root: TreeNode, target_sum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        if root is None:
            return False

        queue = deque([(root, 0)])  # deque([(node, path sum)])

        while queue:
            node, path_sum = queue.popleft()
            if (
                node.left is None and
                node.right is None and
                path_sum + node.val == target_sum
            ):
                return True
            if node.left:
                queue.append((node.left, path_sum + node.val))
            if node.right:
                queue.append((node.right, path_sum + node.val))

        return False


print(Solution().hasPathSum(build_tree([5]), 5) == True)
print(Solution().hasPathSum(build_tree([5, 4, 3]), 8) == True)
print(Solution().hasPathSum(build_tree([5, 4, 3]), 11) == False)
print(Solution().hasPathSum(build_tree([1, 2]), 1) == False)
print(Solution().hasPathSum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True)
print(Solution().hasPathSum(build_tree([1, 2, 3]), 5) == False)
print(Solution().hasPathSum(build_tree([]), 0) == False)
