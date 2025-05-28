# 1, 2, 3, 4, 5, None
# sf
#    s  f
#       s     f 
# 1, 2, 3, 4, None
# sf 
#    s  f
#       s     f


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        """
        # find middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second part (always even size)
        prev = None
        node = slow.next
        slow.next = None  # Cut the list into two halves
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        
        # reorder
        left = head
        right = prev
        while right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next

        return head


print(get_linked_list_values(Solution().reorderList(build_linked_list([1, 2, 3, 4]))) == [1, 4, 2, 3])
print(get_linked_list_values(Solution().reorderList(build_linked_list([1, 2, 3, 4, 5]))) == [1, 5, 2, 4, 3])