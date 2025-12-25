from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: linked list
            A: iteration
        """
        if head.next is None:
            return True

        slow = head
        fast = head.next

        # Find the end of the left potrion.
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        # Reverse the right portion.
        node = slow.next
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next

        # Compare the left and right portions.
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


print(Solution().isPalindrome(build_linked_list([5, 5])) == True)
print(Solution().isPalindrome(build_linked_list([4, 5])) == False)
print(Solution().isPalindrome(build_linked_list([1, 2, 2, 1])) == True)
print(Solution().isPalindrome(build_linked_list([1, 2, 1])) == True)
print(Solution().isPalindrome(build_linked_list([1, 2, 3, 3, 2, 1])) == True)
print(Solution().isPalindrome(build_linked_list([5])) == True)
