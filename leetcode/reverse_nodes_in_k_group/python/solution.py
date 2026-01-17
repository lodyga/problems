from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        if k == 1:
            return head

        def get_kth_or_none_from_current_node(node: ListNode, k: int) -> ListNode:
            while node and k:
                node = node.next
                k -= 1
            return node

        def reverse_k_nodes_from_curren_node(node: ListNode, k: int) -> ListNode:
            prev = None
            while k:
                node_next = node.next
                node.next = prev
                prev = node
                node = node_next
                k -= 1
            return node

        anchor = ListNode(None, head)
        prev = anchor
        node = head

        while True:
            kth_node = get_kth_or_none_from_current_node(node, k - 1)
            prev.next = kth_node or node
            if kth_node is None:
                break

            next_start_node = reverse_k_nodes_from_curren_node(node, k)
            prev = node
            node = next_start_node

        return anchor.next


print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 2), build_linked_list([2, 1, 4, 3, 5])))
print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 3), build_linked_list([3, 2, 1, 4, 5])))
print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 1), build_linked_list([1, 2, 3, 4, 5])))
print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 5), build_linked_list([5, 4, 3, 2, 1])))
print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 4), build_linked_list([4, 3, 2, 1, 5])))
print(are_linked_lists_equeal(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4]), 2), build_linked_list([2, 1, 4, 3])))
