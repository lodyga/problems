from linked_list_utils import *
import heapq


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Time complexity: O(nlogk)
            n: total list nodes conunt
            k: list length
        Auxiliary space complexity: O(logk)
        Tags:
            DS: linked list, merge sort, divide and conquer
            A: recursion
        """
        def merge_two_lists(node1: ListNode, node2: ListNode) -> ListNode:
            node = anchor = ListNode()

            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
                else:
                    node.next = node2
                    node = node.next
                    node2 = node2.next

            node.next = node1 or node2
            return anchor.next

        if len(lists) == 0:
            return ListNode()
        elif len(lists) == 1:
            return lists[0]

        # merge
        return merge_two_lists(
            # divide
            self.mergeKLists(lists[: len(lists) // 2]),
            self.mergeKLists(lists[len(lists) // 2:])
        )


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Time complexity: O(nlogk)
            n: total list nodes count
            k: list length
        Auxiliary space complexity: O(k)
        Tags:
            DS: linked list, heap
            A: iteration
        """
        node_heap = []
        anchor = node = ListNode()

        for head in lists:
            if head:
                heapq.heappush(node_heap, (head.val, id(head), head))

        while node_heap:
            _, _, next_node = heapq.heappop(node_heap)
            node.next = next_node
            node = node.next

            if node.next:
                heapq.heappush(
                    node_heap,
                    (node.next.val, id(node.next), node.next)
                )

        return anchor.next


class Solution2:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Time complexity: O(nlogk)
            n: total list nodes conunt
            k: list length
        Auxiliary space complexity: O(logk)
        Tags:
            DS: linked list, merge sort, divide and conquer
            A: iteration
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

            for idx in range(0, len(lists), 2):
                head1 = lists[idx]
                head2 = lists[idx + 1] if idx + 1 < len(lists) else None
                merged_lists.append(merge_two_lists(head1, head2))

            lists = merged_lists

        return lists[0]


class Solution2:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration,  merge one by one
        """
        if len(lists) == 0:
            return

        anchor = node = ListNode()
        node1 = lists[0]

        for idx in range(1, len(lists)):
            node2 = lists[idx]

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


print(LinkedList().are_linked_lists_equeal(Solution().mergeKLists([LinkedList().build_linked_list([4, 5]), LinkedList().build_linked_list([3, 4])]), LinkedList().build_linked_list([3, 4, 4, 5])))
print(LinkedList().are_linked_lists_equeal(Solution().mergeKLists([LinkedList().build_linked_list([1, 4, 5]), LinkedList().build_linked_list([1, 3, 4]), LinkedList().build_linked_list([2, 6])]), LinkedList().build_linked_list([1, 1, 2, 3, 4, 4, 5, 6])))
# print(are_linked_lists_equeal(Solution().mergeKLists([build_linked_list([4, 5]), build_linked_list([3, 4])]), build_linked_list([3, 4, 4, 5])))
# print(are_linked_lists_equeal(Solution().mergeKLists([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]), build_linked_list([1, 1, 2, 3, 4, 4, 5, 6])))
# print(are_linked_lists_equeal(Solution().mergeKLists([build_linked_list([1, 4, 5])]), build_linked_list([1, 4, 5])))
# print(are_linked_lists_equeal(Solution().mergeKLists([build_linked_list([])]), build_linked_list([])))
# print(are_linked_lists_equeal(Solution().mergeKLists([build_linked_list([]), build_linked_list([0, 5, 11]), build_linked_list([]), build_linked_list([6, 10])]), build_linked_list([0, 5, 6, 10, 11])))

