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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node, targetSum):
            if node is None:
                return False
            elif not node.left and not node.right:
                return targetSum - node.val == 0
            else:
                return (
                    dfs(node.left, targetSum - node.val) or
                    dfs(node.right, targetSum - node.val)
                )

        return dfs(root, targetSum)


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        if not root:
            return False
        
        stack = [(root, targetSum)]

        while stack:
            node, targetSum = stack.pop()

            if (not node.left and 
                not node.right and 
                    targetSum - node.val == 0):
                return True
            if node.right:
                stack.append((node.right, targetSum - node.val))
            if node.left:
                stack.append((node.left, targetSum - node.val))
        
        return False


from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue
        """
        if not root:
            return False
        
        queue = deque([(root, targetSum)])

        while queue:
            node, targetSum = queue.popleft()

            if (not node.left and 
                not node.right and 
                    targetSum - node.val == 0):
                return True
            if node.right:
                queue.append((node.right, targetSum - node.val))
            if node.left:
                queue.append((node.left, targetSum - node.val))
        
        return False


print(Solution().hasPathSum(build_tree([5]), 5) == True)
print(Solution().hasPathSum(build_tree([5, 4, 3]), 8) == True)
print(Solution().hasPathSum(build_tree([5, 4, 3]), 11) == False)
print(Solution().hasPathSum(build_tree([1, 2]), 1) == False)
print(Solution().hasPathSum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True)
print(Solution().hasPathSum(build_tree([1, 2, 3]), 5) == False)
print(Solution().hasPathSum(build_tree([]), 0) == False)