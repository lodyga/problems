from binary_tree_utils import *
import heapq


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, in-order traversal
        """
        vals = []
        
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return vals[k - 1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, list
            A: dfs, recursion, in-order traversal
        """
        numbers = []

        def dfs(node):
            if node is None:
                return
        
            dfs(node.left)

            if len(numbers) < k:
                numbers.append(node.val)
            if len(numbers) == k:
                return

            dfs(node.right)

        dfs(root)
        return numbers[-1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: e
            DS: binary tree
            A: dfs, recursion, in-order traversal
        """
        val = root.val
        
        def dfs(node):
            nonlocal k, val
            if node is None:
                return

            dfs(node.left)
            k -= 1
            if k == 0:
                val = node.val
                return
                
            dfs(node.right)

        dfs(root)
        return val

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, stack, list
            A: dfs, iteration, in-order traversal
        """
        stack = []
        node = root
        
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree, heap
            A: dfs, recursion, pre-order traversal
        """
        nums = []

        def dfs(node):
            if node is None:
                return
            
            if len(nums) < k:
                heapq.heappush(nums, -node.val)
            else:
                heapq.heappushpop(nums, -node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -heapq.heappop(nums)


print(Solution().kthSmallest(build_tree([1]), 1) == 1)
print(Solution().kthSmallest(build_tree([2, 1, 3]), 1) == 1)
print(Solution().kthSmallest(build_tree([1, None, 2]), 2) == 2)
print(Solution().kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3)
print(Solution().kthSmallest(build_tree([5, 3, 7, 2, 4, None, 8]), 3) == 4)
print(Solution().kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1)
print(Solution().kthSmallest(build_tree([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None, None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None, 31, 34, None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5, None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None, 22, None, 14, None, None, 21, 23]), 25) == 24)
