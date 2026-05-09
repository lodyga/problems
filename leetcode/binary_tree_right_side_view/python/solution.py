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
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        from collections import deque
        if root is None:
            return []

        queue = deque([root])
        res = []

        while queue:
            for index in range(len(queue)):
                node = queue.popleft()
                
                if index == 0:
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)

        return res


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, pre-order traversal
        """
        res = []

        def dfs(node, lvl):
            if node is None:
                return
            
            if lvl == len(res):
                res.append(node.val)

            dfs(node.right, lvl + 1)
            dfs(node.left, lvl + 1)
        
        dfs(root, 0)
        return res


print(Solution().rightSideView(build_tree([1, 2, 3])) == [1, 3])
print(Solution().rightSideView(build_tree([1, None, 3])) == [1, 3])
print(Solution().rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4])
print(Solution().rightSideView(build_tree([])) == [])
