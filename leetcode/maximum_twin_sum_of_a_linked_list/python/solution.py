from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: linked list
            A: iteration
        """
        # Find the beginning of the right portion,
        # while reversing the left portion.
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # The reverse
            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next

        # Find max twin.
        left = prev
        right = slow
        twin = 0
        while left:  # or right
            twin = max(twin, left.val + right.val)
            left = left.next
            right = right.next

        return twin


print(Solution().pairSum(build_linked_list([5, 4, 2, 1])) == 6)
print(Solution().pairSum(build_linked_list([4, 2, 2, 3])) == 7)
print(Solution().pairSum(build_linked_list([1, 100000])) == 100001)
