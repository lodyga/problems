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
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
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


console.log(getLinkedListValues(new Solution().reverseList(buildLinkedList([]))), [])
console.log(getLinkedListValues(new Solution().reverseList(buildLinkedList([1, 2]))), [2, 1])
console.log(getLinkedListValues(new Solution().reverseList(buildLinkedList([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])