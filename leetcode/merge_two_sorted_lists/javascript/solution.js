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
    * @param {ListNode} node1
    * @param {ListNode} node2
    * @return {ListNode}
    */
   mergeTwoLists(node1, node2) {
      let node = new ListNode();
      const anchor = node;

      while (node1 && node2) {
         if (node1.val < node2.val) {
            node.next = node1;
            node1 = node1.next;
         } else {
            node.next = node2;
            node2 = node2.next;
         }
         node = node.next;
      }

      node.next = node1 || node2;
      return anchor.next
   }
}


const mergeTwoLists = new Solution().mergeTwoLists;
console.log(areLinkedListsEqueal(new Solution().mergeTwoLists(buildLinkedList([]), buildLinkedList([])), buildLinkedList([])))
console.log(areLinkedListsEqueal(new Solution().mergeTwoLists(buildLinkedList([]), buildLinkedList([0])), buildLinkedList([0])))
console.log(areLinkedListsEqueal(new Solution().mergeTwoLists(buildLinkedList([1, 2, 4]), buildLinkedList([1, 3, 4])), buildLinkedList([1, 1, 2, 3, 4, 4])))
