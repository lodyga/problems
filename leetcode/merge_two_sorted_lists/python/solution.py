from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        node1 = head1
        node2 = head2
        anchor = node = ListNode()

        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            
            node = node.next
        
        node.next = node1 or node2
        return anchor.next


print(get_linked_list_values(Solution().mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4])
print(are_linked_lists_equeal(Solution().mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4])), build_linked_list([1, 1, 2, 3, 4, 4])))
print(are_linked_lists_equeal(Solution().mergeTwoLists(build_linked_list([]), build_linked_list([0])), build_linked_list([0])))
print(are_linked_lists_equeal(Solution().mergeTwoLists(build_linked_list([]), build_linked_list([])), build_linked_list([])))
