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
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth,
                       right_depth)


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, stack, iteration, pre-order traversal
        """
        if not root:
            return 0
        
        max_depth = 1
        stack = [(root, max_depth)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, deque, iteration, level-order traversal
        """
        if not root:
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
