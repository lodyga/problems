class Solution:
    def mergeTwoLists(self, node_1: ListNode, node_2: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        anchor = node = ListNode()

        while node_1 and node_2:
            if node_1.val <= node_2.val:
                node.next = node_1
                node_1 = node_1.next
            else:
                node.next = node_2
                node_2 = node_2.next
            node = node.next

        node.next = node_1 or node_2
        return anchor.next


print(get_linked_list_values(Solution().mergeTwoLists(build_linked_list([]), build_linked_list([]))) == [])
print(get_linked_list_values(Solution().mergeTwoLists(build_linked_list([]), build_linked_list([0]))) == [0])
print(get_linked_list_values(Solution().mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4])