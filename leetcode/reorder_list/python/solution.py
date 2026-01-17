from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: two pointers
        """
        slow = head
        fast = head

        # Find the left end.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the right portion
        node = slow.next
        slow.next = None  # Cut the list into two halves
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        
        # Merge the left and right portions.
        left = head
        right = prev
        while right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next

        return head


print(are_linked_lists_equeal(Solution().reorderList(build_linked_list([1, 2, 3, 4])),build_linked_list([1, 4, 2, 3])))
print(are_linked_lists_equeal(Solution().reorderList(build_linked_list([1, 2, 3, 4, 5])), build_linked_list([1, 5, 2, 4, 3])))
