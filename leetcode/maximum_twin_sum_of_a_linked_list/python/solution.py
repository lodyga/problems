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
        slow = head
        fast = head
        prev = None

        while fast:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next

        left = prev
        right = slow
        res = -1

        while left:
            val = left.val + right.val
            res = max(res, val)
            left = left.next
            right = right.next

        return res


print(Solution().pairSum(build_linked_list([5, 4, 2, 1])) == 6)
print(Solution().pairSum(build_linked_list([4, 2, 2, 3])) == 7)
print(Solution().pairSum(build_linked_list([1, 100000])) == 100001)
