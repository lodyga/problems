from collections import deque


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, queue
            A: bfs, iteration, level-order traversal
        """
        queue = deque([root])

        # bfs
        while queue:
            node_next = None
            
            if queue[0] is None:
                break
            
            for _ in range(len(queue)):
                node = queue.popleft()
                node.next = node_next
                node_next = node
                queue.append(node.right)
                queue.append(node.left)

        return root