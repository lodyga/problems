import { ListNode, areLinkedListsEqueal, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'


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
    * @param {number} val
    * @return {ListNode}
    */
   removeElements(head, val) {
      const anchor = new ListNode(null, head);
      let node = anchor;

      while (node.next) {
         if (node.next.val === val) {
            node.next = node.next.next;
         } else {
            node = node.next;
         }
      }
      return anchor.next
   };
}


const removeElements = new Solution().removeElements;
console.log(areLinkedListsEqueal(new Solution().removeElements(buildLinkedList([1, 2, 6, 3, 4, 5, 6]), 6), buildLinkedList([1, 2, 3, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().removeElements(buildLinkedList([]), 1), buildLinkedList([])))
console.log(areLinkedListsEqueal(new Solution().removeElements(buildLinkedList([7, 7, 7, 7]), 7), buildLinkedList([])))
