class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: linked list
        """
        node = head
        palindrome_lenght = 0

        while node:
            palindrome_lenght += 1
            node = node.next
        
        middle = palindrome_lenght // 2

        # find the end of the left potrion
        node = head
        for _ in range(middle):
            node = node.next

        # if palindrome lenght is odd, skipp the middle node
        if palindrome_lenght % 2:
            node = node.next
        
        # reverse the right portion
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next

        # compare both portions
        left_node = head
        right_node = prev
        while right_node:
            if left_node.val != right_node.val:
                return False
            left_node = left_node.next
            right_node = right_node.next

        return True


print(Solution().isPalindrome(build_linked_list([5, 5])), True)
print(Solution().isPalindrome(build_linked_list([4, 5])), False)
print(Solution().isPalindrome(build_linked_list([1, 2, 2, 1])), True)
print(Solution().isPalindrome(build_linked_list([1, 2, 1])), True)