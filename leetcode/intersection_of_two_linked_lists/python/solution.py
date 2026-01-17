from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: two pointers
        """
        if head_a and head_b is None:
            return head_a and head_b
        
        node_a = head_a
        node_b = head_b
        
        while node_a != node_b:
            node_a = node_a.next if node_a else head_b
            node_b = node_b.next if node_b else head_a
        
        return node_a


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        def get_length(node):
            list_length = 0            
            while node:
                list_length += 1
                node = node.next
            return list_length

        list_a_length = get_length(head_a)
        list_b_length = get_length(head_b)
        length_diff = abs(list_a_length - list_b_length)
        node_a = head_a
        node_b = head_b
        
        if list_a_length > list_b_length:
            for _ in range(length_diff):
                node_a = node_a.next
        elif list_b_length > list_a_length:
            for _ in range(length_diff):
                node_b = node_b.next

        while node_a and node_b:
            if node_a == node_b:
                return node_a
            else:
                node_a = node_a.next
                node_b = node_b.next

        return None