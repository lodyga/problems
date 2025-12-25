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
    *     DS: linked list, two pointers
    *     A: iteration
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode}
    */
   swapNodes(head, k) {
      let slow = head;
      let fast = head;

      for (let index = 1; index < k; index++) {
         fast = fast.next;
      }
      const left = fast;

      while (fast && fast.next) {
         slow = slow.next;
         fast = fast.next;
      }
      const right = slow;

      [left.val, right.val] = [right.val, left.val];
      return head
   };
}


const swapNodes = new Solution().swapNodes;
console.log(areLinkedListsEqueal(new Solution().swapNodes(buildLinkedList([1, 2, 3, 4]), 2), buildLinkedList([1, 3, 2, 4])))
console.log(areLinkedListsEqueal(new Solution().swapNodes(buildLinkedList([1, 2, 3, 4, 5]), 2), buildLinkedList([1, 4, 3, 2, 5])))
console.log(areLinkedListsEqueal(new Solution().swapNodes(buildLinkedList([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5), buildLinkedList([7, 9, 6, 6, 8, 7, 3, 0, 9, 5])))
