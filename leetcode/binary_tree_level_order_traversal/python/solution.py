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
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue, level order traversal
        """
        nodes = []
        queue = deque([root])

        while queue:
            node_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    node_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if node_level:
                nodes.append(node_level)

        return nodes


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, level order traversal
        """
        nodes = []

        def dfs(index, node):
            if not node:
                return
            elif index == len(nodes):
                nodes.append([])

            nodes[index].append(node.val)
            dfs(index + 1, node.left)
            dfs(index + 1, node.right)

        dfs(0, root)
        return nodes


print(Solution().levelOrder(build_tree([1, 2, 3])), [[1], [2, 3]])
print(Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])), [[3], [9, 20], [15, 7]])
print(Solution().levelOrder(build_tree([1])), [[1]])
print(Solution().levelOrder(build_tree([])), [])