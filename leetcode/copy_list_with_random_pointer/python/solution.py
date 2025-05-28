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
        Tags: linked list, hash map
        """
        node = head
        original_to_copy = {None: None}
        while node:
            original_to_copy[node] = Node(node.val)
            node = node.next
            
        node = head
        while node:
            original_to_copy[node].next = original_to_copy[node.next]
            original_to_copy[node].random = original_to_copy[node.random]
            node = node.next

        return original_to_copy[head]