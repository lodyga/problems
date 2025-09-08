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
    def isSameTree(self, root_1: TreeNode | None, root_2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node_1, node_2):
            if not node_1 and not node_2:
                return True
            elif (not node_1 or
                  not node_2 or
                  node_1.val != node_2.val):
                return False

            return (dfs(node_1.left, node_2.left) and
                    dfs(node_1.right, node_2.right))

        return dfs(root_1, root_2)


class Solution:
    def isSameTree(self, root_1: TreeNode | None, root_2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        stack_1 = [root_1]
        stack_2 = [root_2]

        while stack_1 or stack_2:
            node_1 = stack_1.pop()
            node_2 = stack_2.pop()

            if not node_1 and not node_2:
                continue
            elif (not node_1 or
                  not node_2 or
                  node_1.val != node_2.val):
                return False

            stack_1.append(node_1.right)
            stack_2.append(node_2.right)
            stack_1.append(node_1.left)
            stack_2.append(node_2.left)

        return True


class Solution:
    def isSameTree(self, root_1: TreeNode | None, root_2: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue
        """
        queue_1 = deque([root_1])
        queue_2 = deque([root_2])

        while queue_1 or queue_2:
            node_1 = queue_1.popleft()
            node_2 = queue_2.popleft()

            if not node_1 and not node_2:
                continue
            elif (not node_1 or
                  not node_2 or
                  node_1.val != node_2.val):
                return False

            queue_1.append(node_1.left)
            queue_2.append(node_2.left)
            queue_1.append(node_1.right)
            queue_2.append(node_2.right)

        return True


print(Solution().isSameTree(build_tree([]), build_tree([5])) == False)
print(Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) == True)
print(Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) == False)
print(Solution().isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) == False)
print(Solution().isSameTree(build_tree([10, 5, 15]), build_tree([10, 5, None, None, 15])) == False)
print(Solution().isSameTree(build_tree([1, None, 2, 3]), build_tree([1, None, 2, None, 3])) == False)