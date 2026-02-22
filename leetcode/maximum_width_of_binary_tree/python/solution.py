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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, deque
            A: bfs, iteration, level-order traversal
        """
        max_width = 1

        def bfs(node):
            nonlocal max_width
            # deaue([(node, node index), ])
            deq = deque([(node, 0)])

            while deq:
                queue_len = len(deq)

                for index in range(queue_len):
                    node, node_id = deq.popleft()

                    if index == 0:
                        left = node_id
                    if index == queue_len - 1:
                        right = node_id

                    if node.left:
                        deq.append((node.left, node_id * 2 + 1))
                    if node.right:
                        deq.append((node.right, node_id * 2 + 2))

                max_width = max(max_width, right - left + 1)

        bfs(root)
        return max_width


print(Solution().widthOfBinaryTree(build_tree([1])) == 1)
print(Solution().widthOfBinaryTree(build_tree([1, 2, 3])) == 2)
print(Solution().widthOfBinaryTree(build_tree([1, None, 3])) == 1)
print(Solution().widthOfBinaryTree(build_tree([1, 2, None])) == 1)
print(Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5, 3, None, 9])) == 4)
print(Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7)
print(Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5])) == 2)
print(Solution().widthOfBinaryTree(build_tree([1, 1, 1, 1, 1, 1, 1, None, None, None, 1, None, None, None, None, 2, 2, 2, 2, 2, 2, 2, None, 2, None, None, 2, None, 2])) == 8)
