import { areLinkedListsEqueal, buildLinkedList, ListNode } from '../../../../JS/linked-list-utils.js'


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
    * @param {number} x
    * @return {ListNode}
    */
   partition(head, x) {
      const leftAnchor = new ListNode();
      let leftNode = leftAnchor;
      const rightAnchor = new ListNode();
      let rightNode = rightAnchor;
      let node = head;

      while (node) {
         if (node.val < x) {
            leftNode.next = node;
            leftNode = leftNode.next;
         } else {
            rightNode.next = node;
            rightNode = rightNode.next;
         }

         node = node.next;
      }

      rightNode.next = null;
      leftNode.next = rightAnchor.next;
      return leftAnchor.next
   };
}


const partition = new Solution().partition;
console.log(areLinkedListsEqueal(new Solution().partition(buildLinkedList([1, 4, 3, 2, 5, 2]), 3), buildLinkedList([1, 2, 2, 4, 3, 5])))
console.log(areLinkedListsEqueal(new Solution().partition(buildLinkedList([2, 1]), 2), buildLinkedList([1, 2])))
