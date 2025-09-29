from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags: linked list
        merge sort
        """
        if len(lists) == 0:
            return

        def merge_two_lists(node1, node2):
            anchor = node = ListNode()

            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next

            node.next = node1 or node2
            return anchor.next

        while len(lists) > 1:
            merged_lists = []
            for index in range(0, len(lists), 2):
                head1 = lists[index]
                head2 = lists[index + 1] if index + 1 < len(lists) else None
                merged_lists.append(merge_two_lists(head1, head2))
            lists = merged_lists

        return lists[0]


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Time complexity: O(kn)
        Auxiliary space complexity: O(1)
        Tags: linked list
        Merge one by one
        """
        if len(lists) == 0:
            return

        anchor = node = ListNode()
        node1 = lists[0]

        for index in range(1, len(lists)):
            node2 = lists[index]

            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next
            
            node.next = node1 or node2
            node1 = anchor.next
            anchor = node = ListNode()

        return node1


print(get_linked_list_values(Solution().mergeKLists([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])])) == [1, 1, 2, 3, 4, 4, 5, 6])
print(get_linked_list_values(Solution().mergeKLists([build_linked_list([1, 4, 5])])) == [1, 4, 5])
print(get_linked_list_values(Solution().mergeKLists([])) == [])
print(get_linked_list_values(Solution().mergeKLists([build_linked_list([])])) == [])