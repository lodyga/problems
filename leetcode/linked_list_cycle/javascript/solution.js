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
    * Tags: linked list, two pointers, Floyd's tortoise and hare
    * @param {ListNode} head
    * @return {boolean}
    */
   hasCycle(head) {
      let slow = head;
      let fast = head;

      while (fast && fast.next) {
         slow = slow.next;
         fast = fast.next.next;

         if (slow === fast) {
            return true
         }
      }
      return false
   }
}
const hasCycle = new Solution().hasCycle;


console.log(new Solution().hasCycle(buildLinkedList([3, 2, 0, -4], { cyclePosition: 1 })), true)
console.log(new Solution().hasCycle(buildLinkedList([1, 2], { cyclePosition: 0 })), true)
console.log(new Solution().hasCycle(buildLinkedList([1], { cyclePosition: -1 })), false)