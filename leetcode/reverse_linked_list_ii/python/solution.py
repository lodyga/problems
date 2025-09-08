from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        one pass
        """
        anchor = ListNode(None, head)

        # find the left node
        node = anchor
        while left != 0:
            prev_left_node = node
            node = node.next
            left -= 1
            right -= 1
        left_node = node

        # reverse the middle portion
        prev = None
        while right != -1:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
            right -= 1
        
        # link the right side of the reversed portion
        # with the unchanged on the right side
        left_node.next = node
        # link the left side of the reversed portion
        # with the unchanged on the left side
        prev_left_node.next = prev

        return anchor.next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        two pass
        """
        anchor = ListNode(None, head)

        # find the left node
        node = anchor
        while left != 0:
            prev_left_node = node
            node = node.next
            left -= 1
            right -= 1
        left_node = node

        # find the right node
        while right != 0:
            node = node.next
            right -= 1
        right_node = node
        next_right_node = right_node.next

        # traverse to the left node
        node = head
        while node != left_node:
            node = node.next

        # reverse the middle portion
        prev = right_node.next
        while node != next_right_node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next

        prev_left_node.next = prev

        return anchor.next


print(get_linked_list_values(Solution().reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 4)) ==  [1, 4, 3, 2, 5])
print(get_linked_list_values(Solution().reverseBetween(build_linked_list([5]), 1, 1)) == [5])