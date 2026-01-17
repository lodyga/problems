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
        Tags:
            DS: linked list
            A: iteration
        """
        anchor = ListNode(None, head)

        # find the left node
        node = anchor
        index = 1
        while index < left:
            node = node.next
            index += 1
        outer_left = node
        node = node.next
        inner_right = node

        # reverse the middle portion
        prev = None
        while index <= right:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
            index += 1
        
        inner_left = prev
        outer_right = node
        # Link the left side.
        outer_left.next = inner_left
        # Link the right side.
        inner_right.next = outer_right
    
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


print(are_linked_lists_equeal(Solution().reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 4), build_linked_list([1, 4, 3, 2, 5])))
print(are_linked_lists_equeal(Solution().reverseBetween(build_linked_list([5]), 1, 1), build_linked_list([5])))
