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
    def isSameTree(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(root1, root2)


class Solution:
    def isSameTree(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        stack1 = [root1]
        stack2 = [root2]

        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            stack1.append(node1.right)
            stack2.append(node2.right)
            stack1.append(node1.left)
            stack2.append(node2.left)

        return True


class Solution:
    def isSameTree(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue
        """
        queue_1 = deque([root1])
        queue_2 = deque([root2])

        while queue_1 or queue_2:
            node1 = queue_1.popleft()
            node2 = queue_2.popleft()

            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            queue_1.append(node1.left)
            queue_2.append(node2.left)
            queue_1.append(node1.right)
            queue_2.append(node2.right)

        return True


print(Solution().isSameTree(build_tree([]), build_tree([5])) == False)
print(Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) == True)
print(Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) == False)
print(Solution().isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) == False)
print(Solution().isSameTree(build_tree([10, 5, 15]), build_tree([10, 5, None, None, 15])) == False)
print(Solution().isSameTree(build_tree([1, None, 2, 3]), build_tree([1, None, 2, None, 3])) == False)