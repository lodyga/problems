class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} head
    * @return {boolean}
    */
   isPalindrome(head) {
      let node = head;
      let palindrmeLength = 0;

      while (node) {
         palindrmeLength++;
         node = node.next;
      }
      let middle = palindrmeLength / 2 | 0;

      // find the end of the left potrion
      node = head;
      for (let index = 0; index < middle; index++) {
         node = node.next;
      }
      // if palindrome lenght is odd, skipp the middle node
      if (palindrmeLength % 2) {
         node = node.next;
      }

      // reverse the right portion
      let prev = null;
      while (node) {
         const nextNode = node.next;
         node.next = prev;
         prev = node;
         node = nextNode;
      }

      // compare both portions
      let leftNode = head;
      let rightNode = prev;
      while (rightNode) {
         if (leftNode.val != rightNode.val) {
            return false
         }
         leftNode = leftNode.next;
         rightNode = rightNode.next;
      }
      return true
   }
}
const isPalindrome = new Solution().isPalindrome;


console.log(new Solution().isPalindrome(buildLinkedList([5, 5])), true)
console.log(new Solution().isPalindrome(buildLinkedList([4, 5])), false)
console.log(new Solution().isPalindrome(buildLinkedList([1, 2, 2, 1])), true)
console.log(new Solution().isPalindrome(buildLinkedList([1, 2, 1])), true)