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
    * @param {ListNode} head1
    * @param {number} a
    * @param {number} b
    * @param {ListNode} head2
    * @return {ListNode}
    */
   mergeInBetween(head1, a, b, head2) {
      // Traverse to merge start in list 1.
      let node1 = head1;
      for (let index = 0; index < a - 1; index++)
         node1 = node1.next;
      const mergeStart = node1;

      // Traverse to merge end in list 1.
      for (let index = 0; index < b - a + 2; index++)
         node1 = node1.next;
      const mergeEnd = node1;

      // Traverse to end in list 2.
      let node2 = head2;
      while (node2.next)
         node2 = node2.next;

      // Merge 
      mergeStart.next = head2;
      node2.next = mergeEnd;
      return head1
   };
}


const mergeInBetween = new Solution().mergeInBetween;
console.log(areLinkedListsEqueal(new Solution().mergeInBetween(buildLinkedList([10, 1, 13, 6, 9, 5]), 3, 4, buildLinkedList([1000000, 1000001, 1000002])), buildLinkedList([10, 1, 13, 1000000, 1000001, 1000002, 5])))
console.log(areLinkedListsEqueal(new Solution().mergeInBetween(buildLinkedList([0, 1, 2, 3, 4, 5, 6]), 2, 5, buildLinkedList([1000000, 1000001, 1000002, 1000003, 1000004])), buildLinkedList([0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])))
