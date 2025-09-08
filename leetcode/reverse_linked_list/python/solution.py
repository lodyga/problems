from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Reverse a singly-linked list.
        """
        node = head
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Reverse a singly-linked list.
        One-liner
        """
        node = head
        prev = None

        while node:
            node.next, prev, node = prev, node, node.next
        
        return prev


print(get_linked_list_values(Solution().reverseList(build_linked_list([]))) == [])
print(get_linked_list_values(Solution().reverseList(build_linked_list([1, 2]))) == [2, 1])
print(get_linked_list_values(Solution().reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1])