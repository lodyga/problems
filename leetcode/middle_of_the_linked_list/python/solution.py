from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: two pointers
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


print(are_linked_lists_equeal(Solution().middleNode(build_linked_list([1, 2, 3, 4, 5])), build_linked_list([3, 4, 5])))
print(are_linked_lists_equeal(Solution().middleNode(build_linked_list([1, 2, 3, 4, 5, 6])), build_linked_list([4, 5, 6])))
