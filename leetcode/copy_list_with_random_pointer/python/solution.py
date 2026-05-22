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


class Solution:
    def __init__(self):
        # {original node: copy node}
        self.node_map = {None: None}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: linked list, hash map
            A: recursion
        """
        if head in self.node_map:
            return self.node_map[head]

        node_copy = Node(head.val)
        self.node_map[head] = node_copy
        node_copy.next = self.copyRandomList(head.next)
        node_copy.random = self.node_map[head.random]

        return node_copy
