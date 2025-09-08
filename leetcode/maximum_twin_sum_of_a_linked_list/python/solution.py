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
        Tags: linked list
        three pass
        """
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next

        node = slow
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        
        twin_sum = 0
        left = head
        right = prev
        while right:
            twin_sum = max(twin_sum, left.val + right.val)
            left = left.next
            right = right.next

        return twin_sum


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        two pass
        """
        slow = head
        fast = head
        prev = None
        while fast:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow

        twin_sum = 0
        left = prev
        right = slow
        while left:
            twin_sum = max(twin_sum, left.val + right.val)
            left = left.next
            right = right.next

        return twin_sum


print(Solution().pairSum(build_linked_list([5, 4, 2, 1])) == 6)
print(Solution().pairSum(build_linked_list([4, 2, 2, 3])) == 7)
print(Solution().pairSum(build_linked_list([1, 100000])) == 100001)