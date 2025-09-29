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
        Tags: linked list
        """
        if k == 1:
            return head
        
        def find_kth_node(node, k):
            while node and k:
                node = node.next
                k -= 1
            return node
            
        def reverse_k_nodes(node, k):
            prev = None
            while node and k:
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
            kth_node = find_kth_node(node, k - 1)
            if kth_node:
                prev.next = kth_node
            else:
                prev.next = node
                break

            next_start_node = reverse_k_nodes(node, k)
            prev = node
            node = next_start_node
        
        return anchor.next


print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5])
print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5])
print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4, 5])
print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 5)) == [5, 4, 3, 2, 1])
print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4, 5]), 4)) == [4, 3, 2, 1, 5])
print(get_linked_list_values(Solution().reverseKGroup(build_linked_list([1, 2, 3, 4]), 2)) == [2, 1, 4, 3])