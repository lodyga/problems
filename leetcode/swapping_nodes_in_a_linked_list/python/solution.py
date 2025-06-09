class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        three pass
        """
        node = head
        prev = None
        index = 1
        while node:
            if index == k:
                val = node.val
            index += 1
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        
        node = prev
        prev = None
        index = 1
        while node:
            if index == k:
                val, node.val = node.val, val
            index += 1
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        
        node = head
        index = 1
        while node:
            if index == k:
                node.val = val
                break
            index += 1
            node = node.next

        return head


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        two pass
        """
        node = head
        list_length = 0
        while node:
            list_length += 1
            node = node.next

        node = head        
        index = 1
        while node:
            if index == k:
                left = node
            if index == list_length - k + 1:
                right = node
                break
            node = node.next
            index += 1

        left.val, right.val = right.val, left.val
        return head


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list, two pointers
        one pass
        """
        node = left = right = head
        for _ in range(k - 1):
            node = node.next
            left = left.next

        while node.next:
            node = node.next
            right = right.next

        left.val, right.val = right.val, left.val
        return head


print(get_linked_list_values(Solution().swapNodes(build_linked_list([1, 2, 3, 4]), 2)) == [1, 3, 2, 4])
print(get_linked_list_values(Solution().swapNodes(build_linked_list([1, 2, 3, 4, 5]), 2)) == [1, 4, 3, 2, 5])
print(get_linked_list_values(Solution().swapNodes(build_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5])