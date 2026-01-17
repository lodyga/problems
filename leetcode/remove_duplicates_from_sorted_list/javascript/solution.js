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
    * @return {ListNode}
    */
   deleteDuplicates(head) {
      let node = head;

      while (node && node.next) {
         if (node.next.val === node.val) {
            node.next = node.next.next;
         } else {
            node = node.next;
         }
      }
      return head;
   };
}


const deleteDuplicates = new Solution().deleteDuplicates;
console.log(areLinkedListsEqueal(new Solution().deleteDuplicates(buildLinkedList([])), buildLinkedList([])))
console.log(areLinkedListsEqueal(new Solution().deleteDuplicates(buildLinkedList([1, 1, 2])), buildLinkedList([1, 2])))
console.log(areLinkedListsEqueal(new Solution().deleteDuplicates(buildLinkedList([1, 1, 2, 3, 3])), buildLinkedList([1, 2, 3])))
