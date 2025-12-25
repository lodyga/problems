import {ListNode, areLinkedListsEqueal, buildLinkedList, getLinkedListValues} from '../../../../JS/linked-list-utils.js'


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
    *     A: two pointers
    * @param {ListNode} head
    * @param {number} n
    * @return {ListNode}
    */
   removeNthFromEnd(head, n) {
      const anchor = new ListNode(null, head);
      let left = anchor;
      let right = anchor;

      while (n) {
         right = right.next;
         n--;
      }

      while (right.next) {
         left = left.next;
         right = right.next;
      }

      left.next = left.next.next;
      return anchor.next
   };
}


const removeNthFromEnd = new Solution().removeNthFromEnd;
console.log(areLinkedListsEqueal(new Solution().removeNthFromEnd(buildLinkedList([1, 2]), 1), buildLinkedList([1])))
console.log(areLinkedListsEqueal(new Solution().removeNthFromEnd(buildLinkedList([1, 2]), 2), buildLinkedList([2])))
console.log(areLinkedListsEqueal(new Solution().removeNthFromEnd(buildLinkedList([1]), 1), buildLinkedList([])))
console.log(areLinkedListsEqueal(new Solution().removeNthFromEnd(buildLinkedList([1, 2, 3, 4, 5]), 2), buildLinkedList([1, 2, 3, 5])))
