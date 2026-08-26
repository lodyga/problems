from linked_list_utils import *


# class ListNode:
#     """
#     Definition of a node in a singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        node = head
        prev = None

        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next

        return prev


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration
        """
        node = head
        prev = None

        while node:
            node.next, prev, node = prev, node, node.next

        return prev


# linked_list = LinkedList()
# build_linked_list = linked_list.build_linked_list
# get_linked_list_values = linked_list.get_linked_list_values
# are_linked_lists_equeal = linked_list.are_linked_lists_equeal
# solution = Solution()

# print(get_linked_list_values(solution.reverseList(build_linked_list([]))) == [])
# print(get_linked_list_values(solution.reverseList(build_linked_list([1, 2]))) == [2, 1])
# print(get_linked_list_values(solution.reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1])
# print(get_linked_list_values(solution.reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1])
print(LinkedList().get_linked_list_values(Solution().reverseList(LinkedList().build_linked_list([1, 2, 3, 4, 5]))))

#print(are_linked_lists_equeal(solution.reverseList(build_linked_list([1, 2])), build_linked_list([2, 1])))

