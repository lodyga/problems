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
        Tags:
            DS: binary tree, queue, list
            A: bfs, iteration, level-order traversal
        """
        from collections import deque
        
        if root == None:
            return []

        queue = deque([root])
        res = []

        while queue:
            level = []
        
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, pre-order traversal
        """
        res = []

        def dfs(node, level):
            if node is None:
                return
            elif level == len(res):
                res.append([])
            
            res[level].append(node.val)            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res


print(Solution().levelOrder(build_tree([1, 2, 3])) == [[1], [2, 3]])
print(Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]])
print(Solution().levelOrder(build_tree([1])) == [[1]])
print(Solution().levelOrder(build_tree([])) == [])
print(Solution().levelOrder(build_tree([4, 2, 7, 1, 3, 6, 9])) == [[4], [2, 7], [1, 3, 6, 9]])
