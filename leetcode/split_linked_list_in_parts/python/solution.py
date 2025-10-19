from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        div = length // k
        mod = length % k

        node = head
        heads = []
        for _ in range(k):
            heads.append(node)
            if mod:
                rng = div + 1
                mod -= 1
            else:
                rng = div
            
            while rng:
                if rng == 1:
                    node.next, node = None, node.next  # right order
                    # node, node.next = node.next, None  # wrong order
                    # node_next = node.next
                    # node.next = None
                    # node = node_next
                else:
                    node = node.next
                rng -= 1

        return heads


print(Solution().splitListToParts(build_linked_list([1, 2, 3]), 5), )
print(Solution().splitListToParts(build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3), )