class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


print(get_linked_list_values(Solution().middleNode(build_linked_list([1, 2, 3, 4, 5]))), [3, 4, 5])
print(get_linked_list_values(Solution().middleNode(build_linked_list([1, 2, 3, 4, 5, 6]))), [4, 5, 6])