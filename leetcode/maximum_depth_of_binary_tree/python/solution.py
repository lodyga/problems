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
    def maxDepth(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)

        return dfs(root)

    def maxDepth(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal
        """
        if root is None:
            return 0

        max_depth = 1
        stack = [(max_depth, root)]

        while stack:
            depth, node = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((depth + 1, node.right))
            if node.left:
                stack.append((depth + 1, node.left))

        return max_depth

    def maxDepth(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        if root is None:
            return 0

        max_depth = 0
        queue = deque([root])

        while queue:
            max_depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth


print(Solution().maxDepth(build_tree([])) == 0)
print(Solution().maxDepth(build_tree([5])) == 1)
print(Solution().maxDepth(build_tree([1, None, 2])) == 2)
print(Solution().maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3)
print(Solution().maxDepth(build_tree([4, 2, 7, 1, 3, 6, 9])) == 3)
