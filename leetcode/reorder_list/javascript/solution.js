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
    *     A: two pointers
    * @param {ListNode} head
    * @return {ListNode}
    */
   reorderList(head) {
      let slow = head;
      let fast = head;

      while (fast && fast.next) {
         slow = slow.next;
         fast = fast.next.next;
      }

      let node = slow.next;
      slow.next = null;
      let prev = null;
      while (node) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }

      let left = head;
      let right = prev;
      while (right) {
         const leftNext = left.next;
         const rightNext = right.next;
         left.next = right;
         right.next = leftNext;
         left = leftNext;
         right = rightNext;
      }
      return head
   };
}


const reorderList = new Solution().reorderList;
console.log(areLinkedListsEqueal(new Solution().reorderList(buildLinkedList([1, 2, 3, 4])), buildLinkedList([1, 4, 2, 3])))
console.log(areLinkedListsEqueal(new Solution().reorderList(buildLinkedList([1, 2, 3, 4, 5])), buildLinkedList([1, 5, 2, 4, 3])))
