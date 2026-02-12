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
        Tags:
            DS: linked list, list
            A: iteration
        """
        node = head
        length = 0

        while node:
            length += 1
            node = node.next

        part_len = length // k
        rest = length % k

        node = head
        res = []

        for _ in range(k):
            res.append(node)
            
            if node is None:
                continue

            for _ in range(part_len - 1 + (1 if rest else 0)):
                node = node.next

            rest -= 1 if rest else 0
            node_next = node.next
            node.next = None
            node = node_next

        return res


print(Solution().splitListToParts(build_linked_list([1, 2, 3]), 5), )
print(Solution().splitListToParts(build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3), )
