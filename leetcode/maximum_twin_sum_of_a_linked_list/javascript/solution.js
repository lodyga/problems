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
    *    DS: linked list
    *    A: iteration
    * @param {ListNode} head
    * @return {ListNode}
    */
   pairSum(head) {
      // Find the beginning of the right portion,
      // while reversing the left portion.
      let slow = head;
      let fast = head;
      let prev = null;
      while (fast) {
         fast = fast.next.next;
         // The reverse
         const slowNext = slow.next;
         slow.next = prev;
         prev = slow;
         slow = slowNext;
      }

      // Find max twin.
      let twinSum = 0;
      let left = prev;
      let right = slow;
      while (right) {
         twinSum = Math.max(twinSum, left.val + right.val);
         left = left.next;
         right = right.next;
      }
      return twinSum
   };
}


const pairSum = new Solution().pairSum;
console.log(new Solution().pairSum(buildLinkedList([5, 4, 2, 1])) === 6)
console.log(new Solution().pairSum(buildLinkedList([4, 2, 2, 3])) === 7)
console.log(new Solution().pairSum(buildLinkedList([1, 100000])) === 100001)
