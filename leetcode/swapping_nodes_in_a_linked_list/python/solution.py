from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list, two pointers
            A: iteration
        """
        slow = head
        fast = head

        for _ in range(k - 1):
            fast = fast.next
        left = fast

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        right = slow

        left.val, right.val = right.val, left.val
        return head


print(are_linked_lists_equeal(Solution().swapNodes(build_linked_list([1, 2, 3, 4]), 2), build_linked_list([1, 3, 2, 4])))
print(are_linked_lists_equeal(Solution().swapNodes(build_linked_list([1, 2, 3, 4, 5]), 2), build_linked_list([1, 4, 3, 2, 5])))
print(are_linked_lists_equeal(Solution().swapNodes(build_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5), build_linked_list([7, 9, 6, 6, 8, 7, 3, 0, 9, 5])))
