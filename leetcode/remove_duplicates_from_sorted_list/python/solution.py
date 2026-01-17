from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        node = head

        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head


print(are_linked_lists_equeal(Solution().deleteDuplicates(build_linked_list([])), build_linked_list([])))
print(are_linked_lists_equeal(Solution().deleteDuplicates(build_linked_list([1, 1, 2])), build_linked_list([1, 2])))
print(are_linked_lists_equeal(Solution().deleteDuplicates(build_linked_list([1, 1, 2, 3, 3])), build_linked_list([1, 2, 3])))
