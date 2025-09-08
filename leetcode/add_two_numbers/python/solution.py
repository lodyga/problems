from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        anchor = node = ListNode(None)
        carry = 0
        while head1 or head2:
            val = (
                (head1.val if head1 else 0) +
                (head2.val if head2 else 0) +
                carry
            )
            carry = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        
        if carry and not head1 and not head2:
            node.next = ListNode(1)

        return anchor.next


class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: linked list, recursion
        """
        def add(node1, node2, carry):
            if not node1 and not node2 and carry == 0:
                return None
        
            val = (
                (node1.val if node1 else 0) +
                (node2.val if node2 else 0) +
                carry
            )
            carry = val // 10
            val = val % 10
            node = ListNode(val)
            node.next = add(
                node1.next if node1 else None, 
                node2.next if node2 else None, 
                carry)
            return node

        return add(head1, head2, 0)


print(get_linked_list_values(Solution().addTwoNumbers(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4]))) == [7, 0, 8])
print(get_linked_list_values(Solution().addTwoNumbers(build_linked_list([0]), build_linked_list([0]))) == [0])
print(get_linked_list_values(Solution().addTwoNumbers(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9]))) ==  [8, 9, 9, 9, 0, 0, 0, 1])