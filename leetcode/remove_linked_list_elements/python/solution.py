class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        anchor = ListNode(None, head)
        node = anchor

        while node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next
            if node.next:
                node = node.next

        return anchor.next


print(get_linked_list_values(Solution().removeElements(build_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)), [1, 2, 3, 4, 5])
print(get_linked_list_values(Solution().removeElements(build_linked_list([]), 1)), [])
print(get_linked_list_values(Solution().removeElements(build_linked_list([7, 7, 7, 7]), 7)), [])