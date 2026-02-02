from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(nlog min(a, b))
            n: linked list length
            a, b: gcd numbers
        Auxiliary space complexity: O(1)
        Tags:
            DS: linked list
            A: iteration, gcd
        """
        # get_gcd = lambda a, b: get_gcd(b, a % b) if b else a
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        node = head
        while node.next:
            gdc = get_gcd(node.val, node.next.val)
            node.next = ListNode(gdc, node.next)
            node = node.next.next

        return head


print(are_linked_lists_equeal(Solution().insertGreatestCommonDivisors(build_linked_list([7])), build_linked_list([7])))
print(are_linked_lists_equeal(Solution().insertGreatestCommonDivisors(build_linked_list([5, 10])),  build_linked_list([5, 5, 10])))
print(are_linked_lists_equeal(Solution().insertGreatestCommonDivisors(build_linked_list([18, 6, 10, 3])), build_linked_list([18, 6, 6, 2, 10, 1, 3])))
