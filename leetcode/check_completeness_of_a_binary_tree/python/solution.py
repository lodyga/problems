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
    def isCompleteTree(self, root: TreeNode) -> bool:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        queue = deque([root])
        was_none = False

        while queue:
            node = queue.popleft()

            if was_none and node is not None:
                return False

            elif node is None:
                was_none = True
                continue

            queue.append(node.left)
            queue.append(node.right)

        return True


print(Solution().isCompleteTree(build_tree([1, 2, 3, 4, 5, 6])) == True)
print(Solution().isCompleteTree(build_tree([1, 2, 3, 4, 5, None, 7])) == False)
print(Solution().isCompleteTree(build_tree([1])) == True)
print(Solution().isCompleteTree(build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 15])) == False)
