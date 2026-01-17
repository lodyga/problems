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
    * Reverse a singly-linked list.
    * @param {ListNode} head
    * @return {ListNode}
    */
   reverseList(head) {
      let node = head;
      let prev = null;

      while (node) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }
      return prev
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: linked list
    *     A: iteration
    * Reverse a singly-linked list.
    * One-liner
    * @param {ListNode} head
    * @return {ListNode}
    */
   reverseList(head) {
      let node = head;
      let prev = null;

      while (node) {
         [node.next, prev, node] = [prev, node, node.next]
      }
      return prev
   };
}


const reverseList = new Solution().reverseList;
console.log(JSON.stringify(getLinkedListValues(new Solution().reverseList(buildLinkedList([])))) === JSON.stringify([]))
console.log(JSON.stringify(getLinkedListValues(new Solution().reverseList(buildLinkedList([1, 2])))) === JSON.stringify([2, 1]))
console.log(JSON.stringify(getLinkedListValues(new Solution().reverseList(buildLinkedList([1, 2, 3, 4, 5])))) === JSON.stringify([5, 4, 3, 2, 1]))
