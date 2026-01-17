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
        Tags:
            DS: linked list
            A: iteration
        """
        carry = 0
        node1 = head1
        node2 = head2
        anchor = ListNode()
        node = anchor
        
        while node1 or node2 or carry:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            val = val1 + val2 + carry
            val, carry = val % 10, val // 10
            node.next = ListNode(val)
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
            node = node.next
        
        return anchor.next


class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: linked list
            A: recursion
        """
        def dfs(node1: ListNode, node2: ListNode, carry: int) -> ListNode:
            if (
                node1 is None and
                node2 is None and
                carry == 0
            ):
                return None
            
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            val = val1 + val2 + carry
            val, carry = val % 10, val // 10
            node = ListNode(val)
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
            node.next = dfs(node1, node2, carry)
            return node
        
        return dfs(head1, head2, 0)


print(are_linked_lists_equeal(Solution().addTwoNumbers(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4])), build_linked_list([7, 0, 8])))
print(are_linked_lists_equeal(Solution().addTwoNumbers(build_linked_list([0]), build_linked_list([0])), build_linked_list([0])))
print(are_linked_lists_equeal(Solution().addTwoNumbers(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9])), build_linked_list([8, 9, 9, 9, 0, 0, 0, 1])))
