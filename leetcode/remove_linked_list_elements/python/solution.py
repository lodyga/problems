from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        anchor = ListNode(None, head)
        node = anchor

        while node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next
            if node.next:
                node = node.next

        return anchor.next


print(get_linked_list_values(Solution().removeElements(build_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)), [1, 2, 3, 4, 5])
print(get_linked_list_values(Solution().removeElements(build_linked_list([]), 1)), [])
print(get_linked_list_values(Solution().removeElements(build_linked_list([7, 7, 7, 7]), 7)), [])