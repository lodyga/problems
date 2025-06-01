class Solution:
    def mergeInBetween(self, head1: ListNode, a: int, b: int, head2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        anchor = ListNode(None, head1)
        node = anchor
        
        # traverse in to merge start list 1
        while a:
            node = node.next
            a -= 1
            b -= 1
        start_node = node

        # traverse to merge end in list 1
        while b + 2:
            node = node.next
            b -= 1
        end_node = node

        # traverse to end in list 2
        node = head2
        while node.next:
            node = node.next
        node.next = end_node

        # insert start
        start_node.next = head2

        return anchor.next


print(get_linked_list_values(Solution().mergeInBetween(build_linked_list([10, 1, 13, 6, 9, 5]), 3, 4, build_linked_list([1000000, 1000001, 1000002]))) == [10, 1, 13, 1000000, 1000001, 1000002, 5])
print(get_linked_list_values(Solution().mergeInBetween(build_linked_list([0, 1, 2, 3, 4, 5, 6]), 2, 5, build_linked_list([1000000, 1000001, 1000002, 1000003, 1000004]))) == [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])