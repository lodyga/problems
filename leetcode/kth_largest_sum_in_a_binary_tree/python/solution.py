from binary_tree_utils import *
from collections import deque
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
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue, heap
            A: bfs, iteration, level-order traversal
        """
        queue = deque([root])
        min_heap = []

        # bfs
        while queue:
            row_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                row_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(min_heap) < k:
                heapq.heappush(min_heap, row_sum)
            else:
                heapq.heappushpop(min_heap, row_sum)

        return min_heap[0] if len(min_heap) == k else -1


print(Solution().kthLargestLevelSum(build_tree([1, 2, None, 3]), 1) == 3)
print(Solution().kthLargestLevelSum(build_tree([5, 8, 9, 2, 1, 3, 7, 4, 6]), 2) == 13)
print(Solution().kthLargestLevelSum(build_tree([5, 8, 9, 2, 1, 3, 7]), 4) == -1)
