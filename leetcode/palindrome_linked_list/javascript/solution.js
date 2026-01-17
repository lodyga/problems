import { ListNode, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'


/**
 * Represents a node in a singly-linked list.
 * class ListNode {
 *    constructor(val = null, next = null) {
 *       this.val = val;
 *       this.next = next;
 *    }
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: linked list
    *     A: iteration
    * @param {ListNode} head
    * @return {boolean}
    */
   isPalindrome(head) {
      if (head.next === null)
         return true
      let slow = head;
      let fast = head.next;

      // Find the end of the left potrion.
      while (fast.next) {
         slow = slow.next;
         fast = fast.next;
         if (fast.next)
            fast = fast.next;
      }

      // Reverse the right portion.
      let node = slow.next;
      let prev = null;
      while (node) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }

      // Compare the left and right portions.
      let left = head;
      let right = prev;
      while (right) {
         if (left.val != right.val) {
            return false
         }
         left = left.next;
         right = right.next;
      }
      return true
   }
}


const isPalindrome = new Solution().isPalindrome;
console.log(new Solution().isPalindrome(buildLinkedList([5, 5])) === true)
console.log(new Solution().isPalindrome(buildLinkedList([4, 5])) === false)
console.log(new Solution().isPalindrome(buildLinkedList([1, 2, 2, 1])) === true)
console.log(new Solution().isPalindrome(buildLinkedList([1, 2, 1])) === true)
console.log(new Solution().isPalindrome(buildLinkedList([1, 2, 3, 3, 2, 1])) === true)
console.log(new Solution().isPalindrome(buildLinkedList([5])) === true)
