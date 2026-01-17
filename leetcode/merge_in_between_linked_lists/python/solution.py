from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeInBetween(self, head1: ListNode, a: int, b: int, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        # Traverse to merge start in list 1.
        node1 = head1
        for _ in range(a - 1):
            node1 = node1.next
        merge_start = node1

        # Traverse to merge end in list 1.
        for _ in  range(b - a + 2):
            node1 = node1.next
        merge_end = node1

        # Traverse to end in list 2.
        node2 = head2
        while node2.next:
            node2 = node2.next
        
        # Merge 
        merge_start.next = head2
        node2.next = merge_end
        return head1


print(are_linked_lists_equeal(Solution().mergeInBetween(build_linked_list([10, 1, 13, 6, 9, 5]), 3, 4, build_linked_list([1000000, 1000001, 1000002])), build_linked_list([10, 1, 13, 1000000, 1000001, 1000002, 5])))
print(are_linked_lists_equeal(Solution().mergeInBetween(build_linked_list([0, 1, 2, 3, 4, 5, 6]), 2, 5, build_linked_list([1000000, 1000001, 1000002, 1000003, 1000004])), build_linked_list([0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])))
