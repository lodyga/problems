from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, stack, iteration, pre-order traversal
        """
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, deque, iteration
        """
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


print(get_tree_values(Solution().invertTree(build_tree([2, 1, 3]))) == [2, 3, 1])
print(get_tree_values(Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1])
print(get_tree_values(Solution().invertTree(build_tree([7, 3, 15, None, None, 9, 20]))) == [7, 15, 3, 20, 9])
print(get_tree_values(Solution().invertTree(build_tree([]))) == [])