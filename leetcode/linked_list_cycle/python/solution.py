class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers, Floyd's tortoise and hare
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


print(Solution().hasCycle(build_linked_list([3, 2, 0, -4], cycle_position=1)) == True)
print(Solution().hasCycle(build_linked_list([1, 2], cycle_position=0)) == True)
print(Solution().hasCycle(build_linked_list([1], cycle_position=-1)) == False)