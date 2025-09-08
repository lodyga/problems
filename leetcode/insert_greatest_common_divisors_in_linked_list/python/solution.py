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
            a, b: numbers for gcd
        Auxiliary space complexity: O(1)
        Tags: linked list, gcd
        """
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # def get_gcd(a, b):
        #     return get_gcd(b, a % b) if b else a

        node = head
        while node.next:
            next_node = node.next
            gcd = get_gcd(node.val, next_node.val)
            new_node = ListNode(gcd, next_node)
            node.next = new_node
            node = next_node

        return head


print(get_linked_list_values(Solution().insertGreatestCommonDivisors(build_linked_list([7]))), [7])
print(get_linked_list_values(Solution().insertGreatestCommonDivisors(build_linked_list([5, 10]))), [5, 5, 10])
print(get_linked_list_values(Solution().insertGreatestCommonDivisors(build_linked_list([18, 6, 10, 3]))), [18, 6, 6, 2, 10, 1, 3])