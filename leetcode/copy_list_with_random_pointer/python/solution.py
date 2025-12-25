class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: linked list, hash map
            A: iteration
        """
        # {original node: copy node, ...}
        node_map = {None: None}

        node = head
        while node:
            node_copy = Node(node.val)
            node_map[node] = node_copy
            node = node.next

        node = head
        while node:
            node_copy = node_map[node]
            node_copy.next = node_map[node.next]
            node_copy.random = node_map[node.random]
            node = node.next
        
        return node_map[head]