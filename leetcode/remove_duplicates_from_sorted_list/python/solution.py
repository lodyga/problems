class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        node = head

        while node and node.next:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            if node.next:
                node = node.next
        
        return head


print(get_linked_list_values(Solution().deleteDuplicates(build_linked_list([]))) == [])
print(get_linked_list_values(Solution().deleteDuplicates(build_linked_list([1, 1, 2]))) == [1, 2])
print(get_linked_list_values(Solution().deleteDuplicates(build_linked_list([1, 1, 2, 3, 3]))) == [1, 2, 3])