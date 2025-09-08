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
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True
            elif (node.val >= upper_bound or
                    node.val <= lower_bound):
                return False
            else:
                return (
                    dfs(node.left, lower_bound, node.val) and
                    dfs(node.right, node.val, upper_bound))
            
        return dfs(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue
        """
        node = root
        lower_bound = float("-inf")
        upper_bound = float("inf")
        queue = deque([(node, lower_bound, upper_bound)])

        while queue:
            for _ in range(len(queue)):
                node, lower_bound, upper_bound = queue.popleft()

                if (node.val <= lower_bound or 
                        node.val >= upper_bound):
                    return False

                if node.left:
                    queue.append((node.left, lower_bound, min(node.val, upper_bound)))
                if node.right:
                    queue.append((node.right, max(node.val, lower_bound), upper_bound))
        
        return True


print(Solution().isValidBST(build_tree([2, 1, 3])) == True)
print(Solution().isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) == False)
print(Solution().isValidBST(build_tree([2, 2, 2])) == False)
print(Solution().isValidBST(build_tree([0, -1])) == True)
print(Solution().isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) == False)