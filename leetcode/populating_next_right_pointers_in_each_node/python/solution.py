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
        def bfs(node):
            queue = deque([node])

            while queue:
                next_node = None
                
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node is None:
                        return root
                    
                    node.next = next_node
                    next_node = node
                    queue.append(node.right)
                    queue.append(node.left)

        return bfs(root)