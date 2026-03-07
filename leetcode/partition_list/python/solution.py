from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: two pointers
        """
        left_anchor = left_node = ListNode()
        right_anchor = right_node = ListNode()
        node = head

        while node:
            if node.val < x:
                left_node.next = node
                left_node = left_node.next
            else:
                right_node.next = node
                right_node = right_node.next

            node = node.next

        right_node.next = None
        left_node.next = right_anchor.next
        return left_anchor.next


print(are_linked_lists_equeal(Solution().partition(build_linked_list([1, 4, 3, 2, 5, 2]), 3), build_linked_list([1, 2, 2, 4, 3, 5])))
print(are_linked_lists_equeal(Solution().partition(build_linked_list([2, 1]), 2), build_linked_list([1, 2])))
