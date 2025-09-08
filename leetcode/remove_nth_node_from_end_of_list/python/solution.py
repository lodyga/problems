from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        """
        anchor = ListNode(None, head)
        slow = anchor
        fast = head
        
        while n:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return anchor.next


print(get_linked_list_values(Solution().removeNthFromEnd(build_linked_list([1, 2]), 1)) == [1])
print(get_linked_list_values(Solution().removeNthFromEnd(build_linked_list([1, 2]), 2)) == [2])
print(get_linked_list_values(Solution().removeNthFromEnd(build_linked_list([1]), 1)) == [])
print(get_linked_list_values(Solution().removeNthFromEnd(build_linked_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5])