import {ListNode, buildLinkedList, getLinkedListValues} from '../../../../JS/linked-list-utils.js'


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
    * Tags: linked list, two pointers
    * @param {ListNode} head
    * @param {number} n
    * @return {ListNode}
    */
   removeNthFromEnd(head, n) {
      const anchor = new ListNode(null, head);
      let left = anchor;
      let right = head;

      while (n) {
         right = right.next;
         n--;
      }

      while (right) {
         left = left.next;
         right = right.next;
      }

      left.next = left.next.next;

      return anchor.next
   };
}
const removeNthFromEnd = new Solution().removeNthFromEnd;


console.log(getLinkedListValues(new Solution().removeNthFromEnd(buildLinkedList([1, 2]), 1)), [1])
console.log(getLinkedListValues(new Solution().removeNthFromEnd(buildLinkedList([1, 2]), 2)), [2])
console.log(getLinkedListValues(new Solution().removeNthFromEnd(buildLinkedList([1]), 1)), [])
console.log(getLinkedListValues(new Solution().removeNthFromEnd(buildLinkedList([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5])