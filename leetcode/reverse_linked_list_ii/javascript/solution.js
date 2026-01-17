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
    * Tags: linked list
    * @param {ListNode} head
    * @param {number} left
    * @param {number} right
    * @return {ListNode}
    */
   reverseBetween(head, left, right) {
      const anchor = new ListNode(null, head);

      // find the left node
      let node = anchor;
      let prevLeftNode;
      while (left !== 0) {
         prevLeftNode = node;
         node = node.next;
         left--;
         right--;
      }
      const leftNode = node;
      
      // reverse the middle portion
      let prev = null;
      while (right !== - 1) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
         right--;
      }
      // Link the left side.
      leftNode.next = node;
      // Link the right side.
      prevLeftNode.next = prev;
      return anchor.next
   };
}


const reverseBetween = new Solution().reverseBetween;
console.log(areLinkedListsEqueal(new Solution().reverseBetween(buildLinkedList([1, 2, 3, 4, 5]), 2, 4), buildLinkedList([1, 4, 3, 2, 5])))
console.log(areLinkedListsEqueal(new Solution().reverseBetween(buildLinkedList([5]), 1, 1), buildLinkedList([5])))
