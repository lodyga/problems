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
    def isSameTree(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(root1, root2)

    def isSameTree(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, stack
            A: dfs, recursion, pre-order traversal
        """
        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()
            
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True


    def isSameTree(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        queue = deque([(root1, root2)])

        while queue:
            node1, node2 = queue.popleft()
            
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True


print(Solution().isSameTree(build_tree([]), build_tree([5])) == False)
print(Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) == True)
print(Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) == False)
print(Solution().isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) == False)
print(Solution().isSameTree(build_tree([10, 5, 15]), build_tree([10, 5, None, None, 15])) == False)
print(Solution().isSameTree(build_tree([1, None, 2, 3]), build_tree([1, None, 2, None, 3])) == False)
print(Solution().isSameTree(build_tree([4, 2, 7, 1, 3, 6, 9]), build_tree([4, 2, 7, 1, 3, 6, 9])) == True)
