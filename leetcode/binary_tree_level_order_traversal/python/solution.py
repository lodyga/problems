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
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, queue, list
            A: bfs, iteration, level-order traversal
        """
        if root == None:
            return []

        queue = deque([root])
        nodes = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            nodes.append(level)

        return nodes

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, list
            A: dfs, recursion, pre-order traversal
        """
        nodes = []

        def dfs(index, node):
            if node is None:
                return
            elif index == len(nodes):
                nodes.append([])

            nodes[index].append(node.val)
            dfs(index + 1, node.left)
            dfs(index + 1, node.right)

        dfs(0, root)
        return nodes


print(Solution().levelOrder(build_tree([1, 2, 3])) == [[1], [2, 3]])
print(Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]])
print(Solution().levelOrder(build_tree([1])) == [[1]])
print(Solution().levelOrder(build_tree([])) == [])
print(Solution().levelOrder(build_tree([4, 2, 7, 1, 3, 6, 9])) == [[4], [2, 7], [1, 3, 6, 9]])
